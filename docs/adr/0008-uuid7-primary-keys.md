# 0008: Primary keys: UUID7, made by Python, with PostgreSQL as backup

**Status:** Accepted (2026-11-20)

## Context

- A key is in every table and in every link between tables. Changing it
  after the first migration means rebuilding all of them.
- More godowns, branches and businesses may join later, and records may move
  from one server to another. Number keys from two servers clash.
- Number keys show how many records exist, and can be guessed.
- A form can carry a new record's key before the record is saved, so a
  double tap on a weak signal saves it once (built with step 1,
  `docs/PLAN.md`).
- Measured in the developer's earlier project on 2026-10-26 (Django 6.1,
  PostgreSQL 18.6): with a key made only by PostgreSQL, a record linked to
  another before that one was saved lost its link. With the key made by
  Python as well, every case worked, one by one and in bulk.

## Decision

- **Every model in our apps gets a UUID7 key from `core`'s base model**
  (`apps/core/models.py`):
  - Python makes it when the record is created (`default=uuid.uuid7`);
  - PostgreSQL makes it for a row added outside Django
    (`db_default=UUID7()`).
- A test checks that every model in our apps has this key
  (`tests/test_primary_keys.py`).
- Django's own tables keep number keys. `DEFAULT_AUTO_FIELD` says so.
- People never see or use the key. Booking and bill numbers are separate.

## Consequences

- Records move between servers without new numbers, and records can be
  linked before they are saved.
- A key takes 16 bytes instead of 8, and web addresses are longer.
- A key exists from the start, so "is this record saved?" is never asked as
  "is the key empty?". Django's own `_state.adding` answers it.
