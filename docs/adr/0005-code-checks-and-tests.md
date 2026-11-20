# 0005: Code checks and tests: ruff, pre-commit, pytest-django

**Status:** Accepted (2026-11-20)

## Context

- Tests run by hand get skipped, or run only in part. A style rule nobody
  checks breaks quietly.
- Some rules are easy to forget, so a machine should check them: the writing
  rule (`CONTRIBUTING.md`, Docs), no CSS or JS inside templates, and colours
  and sizes only in the design tokens (ADR-0010).

## Decision

- **ruff** checks and formats all Python. Rules: E, W, F, I, UP, B, DJ, S
  (security mistakes), DTZ (a date or time with no time zone) and RUF032 (a
  Decimal made from a float); lines up to 100 characters. Its settings live
  in `pyproject.toml`.
- **pre-commit** runs before every commit:
  - ruff check (with safe fixes) and ruff format, its version kept the same
    as in `uv.lock`;
  - plain writing in docs, code and the commit message;
  - no inline style, script or event handler in HTML, and no number box;
  - colours and sizes only in `static/css/tokens.css`.
- **pytest** with **pytest-django** runs the tests on a real PostgreSQL test
  database. **pytest-cov** measures coverage. Test settings live in
  `config/settings/test.py`.
- **factory-boy** makes test data, added with the first test that needs it.
- All of these are development-only dependencies (the uv `dev` group).

## Consequences

- The same checks run on every machine; CI runs the same commands.
- A commit can be stopped by a check: fix it and commit again. A person can
  skip the hooks on purpose (`--no-verify`), so CI is the final guard.
- The ruff version is named in two places (`uv.lock` and
  `.pre-commit-config.yaml`); they are updated together.
