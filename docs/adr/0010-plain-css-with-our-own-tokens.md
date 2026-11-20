# 0010: Plain CSS with our own tokens; no CSS framework, no build step

**Status:** Accepted (2026-11-20)

## Context

- The plan asks for a strict Content-Security-Policy, with no CSS or JS
  inside templates, and screens that meet WCAG 2.2 AA (`docs/DESIGN.md`).
- A framework brings its own look. In the developer's earlier project, most
  of the look ended up as overrides on top of Bootstrap, many of them inside
  templates.
- Tailwind needs a build step in development, CI and every deploy, and puts
  long lists of classes in every template, which are hard to review.
- Modern CSS covers layout (grid and flexbox), and HTML has its own elements
  for dialogs and sections that open and close (`<dialog>`, `<details>`).
- The earlier project built its design system this way, measured for
  contrast and 44-pixel taps.

## Decision

- **Plain CSS, no CSS framework, no build step.** Files under `static/` are
  served as they are written.
- **Tokens are CSS custom properties in one file,** `static/css/tokens.css`:
  colour, type, spacing, radius, shadow. Every other file uses tokens only;
  pre-commit refuses a raw colour or size anywhere else (ADR-0005).
- **Cascade layers set the order:** reset, base, components, page. A page
  style then never beats a component by accident.
- **Native HTML first:** `<dialog>` and `<details>`. A small JS module only
  where HTML is not enough (ADR-0011).
- **Only CSS features that are Baseline "widely available".**
- **Fonts and icons are kept in the repo,** never loaded from another site.
  The font must also show Malayalam (ADR-0009).
- **Page-specific CSS** goes in `static/<app>/`, never inside a template.
- **Any CSS library later needs its own ADR.**

## Consequences

- We write every component ourselves, in the UI lab first. The lab page
  (`design/lab/system/`) shows every token and component in every state; it
  is the reference to check before writing a screen.
- Accessibility is our job, not a framework's.
- No framework upgrade can break the screens, and there is none to keep
  updated.
