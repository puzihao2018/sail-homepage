---
layout: default
title: Teaching
permalink: /teaching/
---

# Teaching

We are a strong advocate for free and open sharing of teaching and research artifacts to democratize education worldwide. Course materials are made available online wherever possible.

<section class="teaching">
  {%- assign groups = site.data.courses | group_by: "semester" -%}
  {%- for group in groups -%}
    <h2 class="teaching-semester">{{ group.name }}</h2>
    <div class="course-grid">
      {%- for c in group.items -%}
        <article class="course-card">
          {%- if c.url and c.url != "" -%}
            <a href="{{ c.url }}" class="course-card-link">
          {%- endif -%}
          {%- if c.image -%}
            <div class="course-card-image">
              <img src="{{ c.image }}" alt="{{ c.title }}">
            </div>
          {%- endif -%}
          <div class="course-card-content">
            <div class="course-card-meta">
              {%- if c.code -%}<span class="course-code">{{ c.code }}</span>{%- endif -%}
              <span class="course-level">{{ c.level }}</span>
            </div>
            <h3 class="course-card-title">{{ c.title }}</h3>
            {%- if c.description -%}
              <p class="course-card-desc">{{ c.description }}</p>
            {%- endif -%}
            {%- if c.url and c.url != "" -%}
              <span class="course-card-arrow">View course →</span>
            {%- endif -%}
          </div>
          {%- if c.url and c.url != "" -%}
            </a>
          {%- endif -%}
        </article>
      {%- endfor -%}
    </div>
  {%- endfor -%}
</section>
