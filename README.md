# Lab Website (Jekyll + GitHub Pages)

This is a minimal, **GitHub Pages–compatible** Jekyll site for a research group/lab. 
It uses only plugins whitelisted by GitHub Pages (via the `github-pages` gem).

## Quick start (no local Ruby needed)
1. Create a **new GitHub repository** (public is easiest for Pages).
2. Upload/commit these files to the repo (or drag-and-drop the ZIP contents).
3. Go to **Settings → Pages** and choose:
   - Build from: **GitHub Actions** (recommended) *or* **Deploy from a branch**
   - Branch: `main` (root)  
   GitHub will publish at `https://<your-username>.github.io/<repo-name>/`.
4. Edit content directly on GitHub (Markdown files) or via PRs from students.

### Optional: Custom domain
- Add your domain under **Settings → Pages** (e.g., `lab.yourdomain.org`).
- Create a `CNAME` record in your DNS pointing to `<user>.github.io` or the project URL GitHub provides.

## Local preview (optional)
If you want to run the site locally:
```bash
# Install Ruby (3.x recommended) and Bundler, then:
bundle install
bundle exec jekyll serve
# Visit http://127.0.0.1:4000
```

## Content you’ll likely edit
- `index.md` – landing page
- `people.md` – generated from `_data/leader.yml`, `_data/phds.yml`, `_data/masters.yml`, `_data/interns.yml`, `_data/visitings.yml`
- `publications.md` – generated from `_data/publications.yml`
- `projects.md` – generated from `_data/projects.yml`
- `talks.md` – generated from `_data/talks.yml`
- `teaching.md` – generated from `_data/courses.yml` (supports `description` and `image` for thumbnail cards); individual course pages live in `_courses/`
- `_posts/` – news/blog updates
- `assets/img/` – photos and logos
- `assets/img/course-thumbnails/` – course listing thumbnail images
- `assets/slides/` – lecture slide PDFs
- `_config.yml` – site name, nav, Google Analytics ID, etc.

## Teaching workflow

### Adding a new course to the listing
Open `_data/courses.yml` and append an entry:
```yaml
- semester: "Autumn 2026"
  title: "Computer Architecture"
  code: "7CCE3CAR"
  level: "Postgraduate"
  url: "/teaching/autumn2026-computer-architecture/"   # leave "" until page exists
  description: "One-sentence description shown on the teaching listing."
  # image: "/assets/img/course-thumbnails/computer-architecture.jpg"  # optional thumbnail
```
Newest semester first — the listing groups by semester automatically.
- `description`: Brief summary shown on the course card (recommended)
- `image`: Optional thumbnail path; if omitted, the card displays without an image

### Creating an individual course page
1. Copy an existing file from `_courses/` and rename it:
   ```
   _courses/autumn2026-computer-architecture.md
   ```
   The filename (without `.md`) becomes the URL path.

2. Edit the front matter at the top of the file:
   ```yaml
   ---
   title: "Computer Architecture"
   code: "7CCE3CAR"
   semester: "Autumn 2026"
   level: "Postgraduate"
   description: "One-sentence course description shown in the hero."

   staff:
     - name: "Haiyu Mao"
       role: "Lecturer"
       email: "haiyu.mao@kcl.ac.uk"
       url: "https://hybol1993.github.io/"
       office: "Bush House, S2.07"
       office_hours: "Tue 14:00–15:00 or by appointment"

   schedule:
     - week: 1
       date: "2026-09-29"
       topic: "Introduction & Motivation"
       slides: ""                              # leave blank until ready
       reading: ""
     - week: 2
       date: "2026-10-06"
       topic: "Instruction Set Architecture"
       slides: "/assets/slides/car-w02.pdf"   # add PDF to assets/slides/
       reading: "P&H Chapter 2"
   ---
   ```

3. Below the `---` closing fence, add any free-form Markdown:
   ```markdown
   ## Assessment
   - 40% coursework (3 assignments)
   - 60% written exam

   ## Prerequisites
   Familiarity with basic digital logic.
   ```

4. Update `_data/courses.yml` to set the `url` field for this course.

### Uploading slides
Drop PDF files into `assets/slides/` and reference them in the schedule:
```yaml
slides: "/assets/slides/car-w02.pdf"
```

### Uploading course thumbnails
Course thumbnails are optional but make the teaching listing more visually appealing.
Drop images into `assets/img/course-thumbnails/` and reference them in `courses.yml`:
```yaml
image: "/assets/img/course-thumbnails/hardware-design.jpg"
```
Recommended aspect ratio: ~16:9 or 4:3 landscape. Images are cropped to fit a fixed-height card.

### Publication workflow
Author hyperlinks are injected automatically by GitHub Actions on every push to `main`
(via `nameupdate.py`). To update the known-collaborators list, edit `namelist.txt`:
```
Full Name | https://their-homepage.example.com
```

## Collaboration workflow
- Give students **Write** access (or use forks/PRs).
- Protect `main` (Settings → Branches): require PR + 1 review.
- Students edit Markdown/YAML and open PRs; you review/merge.

## License
MIT (see `LICENSE`).
