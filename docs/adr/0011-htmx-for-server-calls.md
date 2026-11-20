# 0011: htmx 4 for server calls; small JavaScript modules for the rest

**Status:** Accepted (2026-11-20)

## Context

- Django renders every page on the server. Some screens still need one part
  of a page to change without a full reload: what is available while an
  estimate is typed, adding an item to a booking, a payment.
- Written in plain JavaScript, each one needs its own request, page update
  and error handling. That leads to requests written inside templates, and
  rules copied into the browser.
- Django 6.1 has template partials (`{% partialdef %}`), so one template can
  render the whole page or only one part of it (ADR-0003).
- htmx is a small script with no build step. An HTML attribute sends a
  request, and the HTML the server answers with replaces a part of the page.
- htmx 4 runs in the developer's earlier project. Its defaults fit our
  rules: attributes pass to child elements only when marked, form errors
  (422) are shown, and no copies of pages are kept in the browser's storage.

## Decision

- **htmx 4 for every interaction with the server.** The server answers with
  HTML, made by a partial of the same template that renders the full page.
- **Rules and numbers stay on the server.** JavaScript never works out money,
  availability or a rule.
- **Small plain JavaScript modules** in static files, only for what happens
  in the browser alone (sounds, confirmation cards, the camera).
- **Nothing that needs `eval`:** no `hx-on` attributes, no `js:` values, no
  trigger filters. The CSP then needs no `unsafe-eval`.
- **Every POST is a real `<form>` with `{% csrf_token %}`,** with its normal
  `action` and `method`, so it still posts if htmx does not load.
- **An invalid form answers 422** with the form and its errors.
- **The htmx file is kept in the repo** under `static/vendor/htmx/`, at an
  exact version, with a test that checks its checksum. No CDN: the CSP allows
  scripts only from our own site. It is added with the first page that uses
  it.
- **No other front-end library** without its own ADR.

**Why not a framework such as React or Vue:** a second codebase (an API and a
front end), a build step, and rules on both sides. For server-rendered
pages, the cost is far above the benefit.

## Consequences

- Most interactions are a round trip to the server. On a weak signal they
  feel slower than pure JavaScript, so a busy sign shows that work is in
  progress, and a save is never sent twice.
- htmx 4 is new, so AI agents often write htmx 2 habits: attributes inherited
  without `:inherited`, and old event names such as `htmx:afterRequest` (now
  `htmx:after:request`). These fail silently. They are a code rule in
  `CONTRIBUTING.md`, checked in review, and the browser tests cover the key
  flows.
- The pinned htmx file does not update itself. It is updated by hand with
  the monthly dependency updates.
