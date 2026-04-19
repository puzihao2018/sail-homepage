(function () {
  "use strict";

  const filtersRoot = document.querySelector(".pub-filters");
  if (!filtersRoot) return;

  const searchInput = document.getElementById("pub-search");
  const sortSelect = document.getElementById("pub-sort");
  const clearBtn = document.getElementById("pub-clear");
  const emptyMsg = document.querySelector(".pub-empty");
  const items = Array.from(document.querySelectorAll(".pub-item"));
  const yearHeaders = Array.from(document.querySelectorAll(".pub-year"));
  const yearLists = Array.from(document.querySelectorAll(".pub-list"));

  const state = {
    author: new Set(),
    year: new Set(),
    venue: new Set(),
    type: new Set(),
    query: "",
    sort: "newest",
  };

  filtersRoot.addEventListener("click", (e) => {
    const chip = e.target.closest(".pub-filter-chip");
    if (!chip) return;
    const dim = chip.dataset.filter;
    const val = chip.dataset.value;
    if (!dim || !(dim in state) || typeof state[dim].has !== "function") return;
    if (state[dim].has(val)) {
      state[dim].delete(val);
      chip.classList.remove("active");
    } else {
      state[dim].add(val);
      chip.classList.add("active");
    }
    apply();
  });

  let searchTimer = null;
  searchInput.addEventListener("input", () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      state.query = searchInput.value.trim().toLowerCase();
      apply();
    }, 150);
  });

  sortSelect.addEventListener("change", () => {
    state.sort = sortSelect.value;
    apply();
  });

  clearBtn.addEventListener("click", () => {
    state.author.clear();
    state.year.clear();
    state.venue.clear();
    state.type.clear();
    state.query = "";
    state.sort = "newest";
    searchInput.value = "";
    sortSelect.value = "newest";
    filtersRoot.querySelectorAll(".pub-filter-chip.active").forEach((c) => c.classList.remove("active"));
    apply();
  });

  function matches(item) {
    if (state.year.size && !state.year.has(item.dataset.year)) return false;
    if (state.venue.size && !state.venue.has(item.dataset.venue)) return false;
    if (state.type.size && !state.type.has(item.dataset.type)) return false;

    if (state.author.size) {
      const authors = item.dataset.authors;
      let hit = false;
      for (const name of state.author) {
        // Word-boundary match via regex; names are already canonical from namelist.yml.
        const re = new RegExp("(?:^|[^\\p{L}])" + escapeRegex(name) + "(?:$|[^\\p{L}])", "u");
        if (re.test(authors)) { hit = true; break; }
      }
      if (!hit) return false;
    }

    if (state.query) {
      const haystack = (item.dataset.title + " " + item.dataset.authors).toLowerCase();
      if (!haystack.includes(state.query)) return false;
    }
    return true;
  }

  function escapeRegex(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function apply() {
    let visibleTotal = 0;
    for (const item of items) {
      const show = matches(item);
      item.hidden = !show;
      if (show) visibleTotal++;
    }

    // Hide empty year groups
    for (const list of yearLists) {
      const year = list.dataset.year;
      const hasVisible = items.some((i) => i.dataset.year === year && !i.hidden);
      list.hidden = !hasVisible;
      const header = yearHeaders.find((h) => h.dataset.year === year);
      if (header) header.hidden = !hasVisible;
    }

    // Sort within each year list
    for (const list of yearLists) {
      const kids = Array.from(list.querySelectorAll(".pub-item"));
      kids.sort(compareBy(state.sort));
      kids.forEach((k) => list.appendChild(k));
    }

    // Reorder year groups for the global sort (newest/oldest)
    const parent = yearLists[0] && yearLists[0].parentNode;
    if (parent) {
      const pairs = yearHeaders
        .map((h) => ({ year: h.dataset.year, header: h, list: yearLists.find((l) => l.dataset.year === h.dataset.year) }))
        .filter((p) => p.list);
      pairs.sort((a, b) => {
        if (state.sort === "oldest") return Number(a.year) - Number(b.year);
        return Number(b.year) - Number(a.year); // newest + venue both keep newest-year-first grouping
      });
      const emptyEl = emptyMsg;
      pairs.forEach((p) => {
        parent.appendChild(p.header);
        parent.appendChild(p.list);
      });
      if (emptyEl) parent.appendChild(emptyEl);
    }

    emptyMsg.hidden = visibleTotal > 0;
  }

  function compareBy(mode) {
    if (mode === "venue") {
      return (a, b) => a.dataset.venue.localeCompare(b.dataset.venue);
    }
    if (mode === "oldest") {
      return (a, b) =>
        Number(a.dataset.year) - Number(b.dataset.year) ||
        a.dataset.venue.localeCompare(b.dataset.venue);
    }
    // newest (default): within the same year group the order is already build-time; keep stable
    return () => 0;
  }
})();
