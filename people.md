---
layout: default
title: People
permalink: /people/
---

# Group Leader

<div class="card-grid">
{% for m in site.data.leader %}
  <div class="card">
    {% if m.photo %}<img id="{{ m.name | slugify }}" src="{{ m.photo | relative_url }}" alt="{{ m.name }} photo">{% endif %}
    <h3>{{ m.name }}</h3>
    <p class="badge">{{ m.role }}</p>
    {% if m.email %}<p>Email:<br><a href="mailto:{{ m.email }}">{{ m.email }}</a></p>{% endif %}
    {% if m.web %}<p>Homepage: <a href="{{ m.web }}" target="_blank" rel="noopener">Personal</a></p>{% endif %}
    <!-- {% if m.topics %}<p><strong>Interests:</strong> {{ m.topics | join: ", " }}</p>{% endif %} -->
  </div>
{% endfor %}
</div>

# Group Members


<!-- ## PhD Students -->

<div class="card-grid">
{% for m in site.data.phds %}
  <div class="card">
    {% if m.photo %}<img id="{{ m.name | slugify }}" src="{{ m.photo | relative_url }}" alt="{{ m.name }} photo">{% endif %}
    <h3>{{ m.name }}</h3>
    <p class="badge">{{ m.role }}</p>
    {% if m.comment %}<p>{{ m.comment }}</p>{% endif %}
    {% if m.email %}<p>Email:<br><a href="mailto:{{ m.email }}">{{ m.email }}</a></p>{% endif %}
    {% if m.web %}<p><a href="{{ m.web }}" target="_blank" rel="noopener">Personal Homepage</a></p>{% endif %}
    {% if m.topics %}<p><strong>Interests:</strong> {{ m.topics | join: ", " }}</p>{% endif %}
    {% if m.work %}<p><strong>Work:</strong> {{ m.work }}</p>{% endif %}
    {% if m.master %}<p><strong>Master:</strong>  {{ m.master}}</p>{% endif %}
    {% if m.bachelor %}<p><strong>Bachelor:</strong> {{ m.bachelor}}</p>{% endif %}
  </div>
{% endfor %}
</div>

## Interns

<ul class="intern-list">
  {% for m in site.data.interns %}
    <li id="{{ m.name | slugify }}">
      <strong>{{ m.name }}</strong>
      {% if m.degree %} — {{ m.degree }}{% endif %}
      {% if m.affiliation %}, {{ m.affiliation }}{% endif %}
      {% if m.period %} ({{ m.period }}){% endif %}
      {% if m.note %}
        <br><span class="intern-note">{{ m.note }}</span>
      {% endif %}
    </li>
  {% endfor %}
</ul>


<!-- ## Visiting Students

<div class="card-grid">
{% for m in site.data.visitings %}
  <div class="card">
    {% if m.photo %}<img src="{{ m.photo | relative_url }}" alt="{{ m.name }} photo">{% endif %}
    <h3>{{ m.name }}</h3>
    <p class="badge">{{ m.role }}</p>
    {% if m.email %}<p>Email:<br><a href="mailto:{{ m.email }}">{{ m.email }}</a></p>{% endif %}
    {% if m.web %}<p><a href="{{ m.web }}" target="_blank" rel="noopener">Personal Homepage</a></p>{% endif %}
    {% if m.topics %}<p><strong>Interests:</strong> {{ m.topics | join: ", " }}</p>{% endif %}
  </div>
{% endfor %}
</div>


## Master Students

<div class="card-grid">
{% for m in site.data.masters %}
  <div class="card">
    {% if m.photo %}<img src="{{ m.photo | relative_url }}" alt="{{ m.name }} photo">{% endif %}
    <h3>{{ m.name }}</h3>
    <p class="badge">{{ m.role }}</p>
    {% if m.email %}<p>Email:<br><a href="mailto:{{ m.email }}">{{ m.email }}</a></p>{% endif %}
    {% if m.web %}<p><a href="{{ m.web }}" target="_blank" rel="noopener">Personal Homepage</a></p>{% endif %}
    {% if m.topics %}<p><strong>Interests:</strong> {{ m.topics | join: ", " }}</p>{% endif %}
  </div>
{% endfor %}
</div>

## Interns

<div class="card-grid">
{% for m in site.data.interns %}
  <div class="card">
    {% if m.photo %}<img src="{{ m.photo | relative_url }}" alt="{{ m.name }} photo">{% endif %}
    <h3>{{ m.name }}</h3>
    <p class="badge">{{ m.role }}</p>
    {% if m.email %}<p>Email:<br><a href="mailto:{{ m.email }}">{{ m.email }}</a></p>{% endif %}
    {% if m.web %}<p><a href="{{ m.web }}" target="_blank" rel="noopener">Personal Homepage</a></p>{% endif %}
    {% if m.topics %}<p><strong>Interests:</strong> {{ m.topics | join: ", " }}</p>{% endif %}
  </div>
{% endfor %}
</div> -->
