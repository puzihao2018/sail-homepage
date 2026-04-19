---
layout: default
title: Publications
permalink: /publications/
---

# Publications

<section class="pub-filters" aria-label="Publication filters">
  <div class="pub-filter-row">
    <div class="pub-filter-group">
      <span class="pub-filter-label">Author</span>
      <div class="pub-filter-chips">
        {%- for n in site.data.namelist -%}
          <button type="button" class="pub-filter-chip" data-filter="author" data-value="{{ n.name | escape }}">{{ n.name }}</button>
        {%- endfor -%}
      </div>
    </div>

    <div class="pub-filter-group">
      <span class="pub-filter-label">Year</span>
      <div class="pub-filter-chips">
        {%- assign years = site.data.publications | map: "year" | uniq | sort | reverse -%}
        {%- for y in years -%}
          <button type="button" class="pub-filter-chip" data-filter="year" data-value="{{ y }}">{{ y }}</button>
        {%- endfor -%}
      </div>
    </div>

    <div class="pub-filter-group">
      <span class="pub-filter-label">Venue</span>
      <div class="pub-filter-chips">
        {%- assign venues = site.data.publications | map: "venue" | uniq | sort -%}
        {%- for v in venues -%}
          <button type="button" class="pub-filter-chip" data-filter="venue" data-value="{{ v | escape }}">{{ v }}</button>
        {%- endfor -%}
      </div>
    </div>

    <div class="pub-filter-group">
      <span class="pub-filter-label">Type</span>
      <div class="pub-filter-chips">
        <button type="button" class="pub-filter-chip" data-filter="type" data-value="conference">Conference</button>
        <button type="button" class="pub-filter-chip" data-filter="type" data-value="journal">Journal</button>
      </div>
    </div>
  </div>

  <div class="pub-filter-controls">
    <input type="search" id="pub-search" class="pub-search" placeholder="Search title or authors…" autocomplete="off">
    <label class="pub-sort-label">
      Sort
      <select id="pub-sort" class="pub-sort">
        <option value="newest">Newest first</option>
        <option value="oldest">Oldest first</option>
        <option value="venue">Venue A–Z</option>
      </select>
    </label>
    <button type="button" id="pub-clear" class="pub-clear">Clear filters</button>
  </div>
</section>

<section class="pubs">
  {%- assign groups = site.data.publications | group_by: "year" | sort: "name" | reverse -%}

  {%- for year_group in groups -%}
    <h2 class="pub-year" id="y{{ year_group.name }}" data-year="{{ year_group.name }}">{{ year_group.name }}</h2>
    <div class="pub-list" data-year="{{ year_group.name }}">
      {%- for p in year_group.items -%}
        <article class="pub-item"
                 data-year="{{ p.year }}"
                 data-venue="{{ p.venue | escape }}"
                 data-type="{{ p.type }}"
                 data-authors="{{ p.authors | escape }}"
                 data-title="{{ p.title | escape }}">
          <div class="pub-venue">
            {{ p.venue }}
          </div>
          <h3 class="pub-title">
            {{ p.title }}
          </h3>
          <div class="pub-authors">
            {%- assign authors = p.authors | split: ", " -%}
            {%- for author in authors -%}
              {%- assign person = site.data.leader | concat: site.data.phds | concat: site.data.interns | where: "name", author | first -%}
              {%- if person -%}
                <a href="/people/#{{ author | slugify }}" class="sail-link">{{ author }}</a>
              {%- else -%}
                <span class="external-author">{{ author }}</span>
              {%- endif -%}
              {%- unless forloop.last -%}, {% endunless -%}
            {%- endfor -%}
          </div>
          <div class="pub-links">
            {%- if p.pdf -%}
              <a class="pub-btn" href="{{ p.pdf | relative_url }}" target="_blank" rel="noopener">PDF</a>
            {%- endif -%}

            {%- if p.slides -%}
              <a class="pub-btn" href="{{ p.slides | relative_url }}" target="_blank" rel="noopener">Slides</a>
            {%- endif -%}

            {%- if p.poster -%}
              <a class="pub-btn" href="{{ p.poster | relative_url }}" target="_blank" rel="noopener">Poster</a>
            {%- endif -%}

            {%- if p.video -%}
              <a class="pub-btn" href="{{ p.video }}" target="_blank" rel="noopener">Talk</a>
            {%- endif -%}

            {%- if p.code -%}
              <a class="pub-btn" href="{{ p.code }}" target="_blank" rel="noopener">Code</a>
            {%- endif -%}

            {%- if p.doi -%}
              <a class="pub-btn" href="https://doi.org/{{ p.doi }}" target="_blank" rel="noopener">DOI</a>
            {%- endif -%}
          </div>
        </article>
      {%- endfor -%}
    </div>
  {%- endfor -%}

  <p class="pub-empty" hidden>No publications match the current filters.</p>
</section>

<script src="{{ '/assets/js/publications-filter.js' | relative_url }}" defer></script>
