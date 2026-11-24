# Architecture Decision Records

One short file per significant decision: what was decided, why, and what it
costs.

Most of the first decisions were made and tested in the developer's earlier
project, then checked again for this system before they were written here.

| # | Decision | Status |
|---|---|---|
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-python-3-14-and-uv.md) | Python 3.14, managed with uv | Accepted |
| [0003](0003-django-6-1-then-6-2-lts.md) | Django 6.1 now, then 6.2 LTS | Accepted |
| [0004](0004-postgresql-18-on-every-machine.md) | PostgreSQL 18 on every machine; no Docker on the laptop | Accepted |
| [0005](0005-code-checks-and-tests.md) | Code checks and tests: ruff, pre-commit, pytest-django | Accepted |
| [0006](0006-ci-on-github-actions.md) | CI on GitHub Actions | Accepted |
| [0007](0007-apps-in-layers.md) | Apps in layers, with services and selectors, checked by the tests | Accepted |
| [0008](0008-uuid7-primary-keys.md) | Primary keys: UUID7, made by Python, with PostgreSQL as backup | Accepted |
| [0009](0009-translatable-text-from-day-one.md) | Translatable text from day one; Malayalam later | Accepted |
| [0010](0010-plain-css-with-our-own-tokens.md) | Plain CSS with our own tokens; no CSS framework, no build step | Accepted |
| [0011](0011-htmx-for-server-calls.md) | htmx 4 for server calls; small JavaScript modules for the rest | Accepted |
| [0012](0012-ready-for-many-businesses.md) | One codebase, ready for many businesses and branches; SaaS features wait | Proposed |
| [0013](0013-availability-by-time.md) | Availability by time: a booking holds its pieces from loading to back | Proposed |

## Rules

- Write one when a choice is hard to undo, or someone would ask "why?".
- Numbered in order, never reused. File name: `NNNN-short-title.md`.
- Status: `Proposed`, then `Accepted`. Later: `Superseded by NNNN`.
- An accepted ADR is never rewritten. Only its status line changes; a new ADR
  carries the new decision.
- Add every new ADR to the table above.

## Template

```markdown
# NNNN: Title

**Status:** Proposed (YYYY-MM-DD)

## Context
What forces the decision. Facts, not opinions.

## Decision
What we will do. Short and concrete.

## Consequences
What gets easier, what gets harder, what it costs.
```
