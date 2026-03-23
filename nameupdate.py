#!/usr/bin/env python3
"""
nameupdate.py — inject name hyperlinks into _data/publications.yml

Usage:
    python nameupdate.py                       # check consistency (warn) + inject links
    python nameupdate.py --check-only          # report issues, do NOT modify files
    python nameupdate.py --check-only --strict # exit 1 on any issue, do NOT modify files
    python nameupdate.py --strict              # inject links + exit 1 on any issue
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml  # PyYAML — only non-stdlib dependency


# ---------------------------------------------------------------------------
# Core helpers (original logic, preserved)
# ---------------------------------------------------------------------------

def load_namelist(path: Path) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Expect format: <name>, <url>
            parts = [p.strip() for p in line.split(",", 1)]
            if len(parts) != 2:
                continue
            name, url = parts
            if name and url:
                mapping[name] = url
    return mapping


def strip_html_tags(text: str) -> str:
    """Remove anything between < and >, non-greedy to handle nested tags conservatively."""
    return re.sub(r"<[^>]*?>", "", text, flags=re.DOTALL)


def hyperlink_names(text: str, name_url: Dict[str, str]) -> str:
    """Replace longer names first to avoid partial overlaps."""
    for name in sorted(name_url.keys(), key=len, reverse=True):
        url = name_url[name]
        # Use word boundaries around the full name; escape the name for regex safety
        pattern = re.compile(rf"\b({re.escape(name)})\b", flags=re.UNICODE)

        def repl(m: re.Match, _url: str = url) -> str:
            matched = m.group(1)
            # Use single quotes in href to keep YAML double-quoted strings valid
            return f"<a href='{_url}'><u>{matched}</u></a>"

        text = pattern.sub(repl, text)
    return text


def process_publications(repo_root: Path) -> None:
    """Strip existing HTML from publications.yml then re-inject name hyperlinks."""
    namelist_path = repo_root / "namelist.txt"
    publications_path = repo_root / "_data" / "publications.yml"

    if not namelist_path.exists():
        raise FileNotFoundError(f"namelist not found: {namelist_path}")
    if not publications_path.exists():
        raise FileNotFoundError(f"publications.yml not found: {publications_path}")

    name_map = load_namelist(namelist_path)
    original_text = publications_path.read_text(encoding="utf-8")
    cleaned = strip_html_tags(original_text)
    updated = hyperlink_names(cleaned, name_map)
    publications_path.write_text(updated, encoding="utf-8")


# ---------------------------------------------------------------------------
# Consistency checking — new additions
# ---------------------------------------------------------------------------

PEOPLE_FILES = ["leader.yml", "phds.yml", "interns.yml", "masters.yml", "visitings.yml"]


def load_lab_members(repo_root: Path) -> List[str]:
    """
    Return every 'name' field from all people YAML data files.
    Skips files that parse to None or an empty list (e.g. all-comment files).
    """
    data_dir = repo_root / "_data"
    members: List[str] = []
    for filename in PEOPLE_FILES:
        fpath = data_dir / filename
        if not fpath.exists():
            continue
        with fpath.open("r", encoding="utf-8") as f:
            parsed = yaml.safe_load(f)
        if not parsed:
            continue
        for entry in parsed:
            if isinstance(entry, dict) and "name" in entry:
                members.append(entry["name"])
    return members


def load_raw_author_strings(repo_root: Path) -> List[str]:
    """
    Parse publications.yml with PyYAML, extract each 'authors' field,
    and strip any embedded HTML. Returns one clean string per publication.
    Works correctly whether the committed YAML is already clean or HTML-laden.
    """
    pub_path = repo_root / "_data" / "publications.yml"
    with pub_path.open("r", encoding="utf-8") as f:
        pubs = yaml.safe_load(f)
    if not pubs:
        return []
    result = []
    for pub in pubs:
        if isinstance(pub, dict) and "authors" in pub:
            raw = strip_html_tags(str(pub["authors"]))
            result.append(raw)
    return result


def check_consistency(
    repo_root: Path,
    name_map: Dict[str, str],
) -> Tuple[bool, List[str]]:
    """
    Run two consistency checks and return (had_issues, warning_messages).

    Check 1 — Missing coverage:
        A lab member whose name appears in a publication author string
        but is NOT in namelist.txt → their name won't be hyperlinked.

    Check 2 — Stale entries:
        A name in namelist.txt that never appears in any publication
        author string → the entry may be outdated or misspelled.
    """
    namelist_names: Set[str] = set(name_map.keys())
    lab_members = load_lab_members(repo_root)
    author_strings = load_raw_author_strings(repo_root)
    all_authors = "\n".join(author_strings)

    messages: List[str] = []
    had_issues = False

    # Check 1: lab members appearing in publications but missing from namelist
    for member in lab_members:
        if member in namelist_names:
            continue
        if re.search(rf"\b{re.escape(member)}\b", all_authors):
            messages.append(
                f"WARNING [missing-coverage]: '{member}' appears in publications "
                f"but is not in namelist.txt — their name will not be hyperlinked"
            )
            had_issues = True

    # Check 2: namelist entries that never appear in any publication
    for name in sorted(namelist_names):
        if not re.search(rf"\b{re.escape(name)}\b", all_authors):
            messages.append(
                f"WARNING [stale-entry]: '{name}' is in namelist.txt "
                f"but does not appear in any publication author list"
            )
            had_issues = True

    return had_issues, messages


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inject name hyperlinks into _data/publications.yml"
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Run consistency checks only; do NOT modify publications.yml",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if any consistency issue is found",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    namelist_path = repo_root / "namelist.txt"

    if not namelist_path.exists():
        print(f"ERROR: namelist not found: {namelist_path}", file=sys.stderr)
        sys.exit(1)

    name_map = load_namelist(namelist_path)
    had_issues, messages = check_consistency(repo_root, name_map)

    for msg in messages:
        print(msg, file=sys.stderr)

    if not messages:
        print("OK: namelist.txt is consistent with people pages and publications.", file=sys.stderr)

    if args.check_only:
        sys.exit(1 if (had_issues and args.strict) else 0)

    # Default mode: inject hyperlinks into publications.yml
    process_publications(repo_root)
    print("OK: publications.yml updated with name hyperlinks.", file=sys.stderr)

    if had_issues and args.strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
