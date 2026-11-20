# 0002: Python 3.14, managed with uv

**Status:** Accepted (2026-11-20)

## Context

- Django 6.1 supports Python 3.12, 3.13 and 3.14 (its release notes, read on
  2026-10-15).
- The laptop, CI and every server must run exactly the same versions of
  Python and of every library.
- On the development laptop (Windows), `python` opens the Microsoft Store.
- uv 0.13.1 and Python 3.14.8 are already on the laptop, and run the
  developer's earlier project (checked 2026-11-20).

## Decision

- Python 3.14, pinned in `.python-version` and in `requires-python`.
- `uv` manages Python itself, the virtual environment, the dependencies and
  the lock file. `uv.lock` is committed.
- Commands run through `uv run` (for example `uv run python manage.py check`).
  `pip` is not used directly in the project.
- The first lock took the versions already checked in the earlier project.
  A later update locks the exact version that was approved
  (`uv lock --upgrade-package "name==x.y.z"`), never simply the newest.

## Consequences

- One tool instead of several; installs are fast and repeatable.
- The lock file gives the same versions on every machine.
- Moving to Python 3.15 is its own small step, once Django supports it.
