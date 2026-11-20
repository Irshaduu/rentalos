# 0003: Django 6.1 now, then 6.2 LTS

**Status:** Accepted (2026-11-20)

## Context

- Read on djangoproject.com on 2026-10-15: 6.1 is the current release,
  supported until December 2027; 6.2 LTS is planned for April 2027,
  supported until April 2030.
- The 6.x line has a built-in Content-Security-Policy and template partials.
  The plan asks for a strict CSP and simple, htmx-friendly templates
  (ADR-0011).
- Django 6.1.2 runs the developer's earlier project, with its tests passing
  on PostgreSQL 18.

## Decision

- Django 6.1, pinned to the 6.1 series (`>=6.1,<6.2`).
- Move to 6.2 LTS after it is released, as its own small, tested step.
- In production, stay on LTS releases after that.

## Consequences

- One planned upgrade in 2027.
- No separate CSP library is needed.
- Some add-on libraries are slow to support a new Django, so each one is
  checked for 6.1 support before it is added, and gets its own ADR.
