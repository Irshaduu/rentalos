# 0004: PostgreSQL 18 on every machine; no Docker on the laptop

**Status:** Accepted (2026-11-20)

## Context

- The client's first rule: availability is always right. Two bookings saved
  at the same moment must never take the same pieces. That needs a database
  with real row locks and constraints, the same on every machine.
- PostgreSQL 18.6 runs on the laptop as a Windows service (checked
  2026-11-20). Support for 18 ends in November 2030 (postgresql.org, read on
  2026-10-23).
- The laptop has 7.7 GB of memory. Docker would take a large part of it.

## Decision

- **PostgreSQL 18 on every machine:** the laptop, CI and production.
- The laptop runs the Windows service, with this project's own database and
  user (`rentalos`). The user may create databases, so the test runner
  can create its test database.
- No SQLite, not even for tests: they run on PostgreSQL, as the client will.
- Connection settings come from environment variables, read from a local
  `.env` file that is never committed. `.env.example` lists every variable.
- CI uses a `postgres:18` service container.
- The database driver is psycopg 3 (`psycopg[binary]`).
- A test checks that the database is 18 or newer (`tests/test_settings.py`).
- **We use what PostgreSQL 18 offers, where it helps:** constraints (unique,
  check, exclusion), generated fields, database defaults, `UUID7`. It is
  written through Django in `models.py`. Business rules never go into
  triggers or stored procedures: like signals, they hide the flow.

## Consequences

- The tests run on the version the client will run.
- Another developer installs PostgreSQL 18 their own way (or runs it in
  Docker); the settings only read environment variables.
- The backup and restore tools (`pg_dump`, `pg_restore`) must have the same
  major version as the server.
