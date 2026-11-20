# 0007: Apps in layers, with services and selectors, checked by the tests

**Status:** Accepted (2026-11-20)

## Context

- When apps import each other freely, and rules live in views, models,
  signals and template scripts, "where does this rule live?" gets several
  answers. In the developer's earlier project, two large apps imported each
  other.
- This system has clear layers: the business and its users at the base;
  stock and customers; bookings; the godown's work on a booking; bills on
  top.
- import-linter reads `import` lines. A Django link written as text, like
  `ForeignKey("bookings.Booking")`, needs no import, so import-linter cannot
  see one. (import-linter 2.15 was compared with other tools on 2026-10-26,
  in the earlier project: stable, BSD licence, Python 3.14, clear messages.)

## Decision

- One Django project, split into small apps, each with one job. An app is
  created with its first real code: a model, a page or a shared tool. No
  empty apps.
- **Apps are layered** (`docs/ARCHITECTURE.md`). An app imports only from
  apps in lower layers, and its models link only to its own app or to lower
  layers. No generic links (`GenericForeignKey`): PostgreSQL cannot guard
  them (ADR-0004).
- **Inside an app:** `services.py` changes data, `selectors.py` reads it,
  views stay thin, and signals carry no business logic.
- **import-linter checks the imports:** one `layers` contract in
  `pyproject.toml` lists every app, top floor first; apps on one row never
  use each other; an app not built yet is in brackets; `exhaustive` is on,
  so an app folder not placed on a floor fails.
- **Our own test checks the model links,** with the same floors read from
  `pyproject.toml`, so the order has one home. It also fails on a generic
  link. Both run in `tests/test_layers.py`.
- No exception (`ignore_imports`) without a line saying why.

## Consequences

- "Where does this rule live?" has one answer.
- A lower app never reads an upper one. When it needs data that an upper app
  creates, the upper app's service passes it down.
- A new app is placed on its floor in `pyproject.toml` in the same commit.
- More files, and some links between apps need care. Availability reads
  bookings and the godown's returns, so where its counts live is decided in
  its own ADR before it is built.
- No microservices: at this size they would add cost with no benefit.
