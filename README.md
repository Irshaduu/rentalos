# RentalOS

Runs an event equipment rental business: stock, what is available on every
date, estimates and bookings, the godown's loading and return, final bills
and payments.

> **Status: step 0, the setup, is built.** Tools, code checks, CI and the
> safe Django base are in place; there is no business page yet. See
> [the plan](docs/PLAN.md).

## Run it locally

You need [uv](https://docs.astral.sh/uv/) and PostgreSQL 18
([ADR-0002](docs/adr/0002-python-3-14-and-uv.md),
[ADR-0004](docs/adr/0004-postgresql-18-on-every-machine.md)).

1. `uv sync` installs Python 3.14 and every dependency.
2. Copy `.env.example` to `.env` and fill in the values.
3. Create the PostgreSQL user and database named in `.env`. The user needs
   permission to create databases, for the tests.
4. `uv run python manage.py migrate`
5. `uv run python manage.py runserver`

## Checks and tests

- `uv run pre-commit install` once: the checks then run before every commit.
- `uv run pytest` runs the tests.
- `uv run ruff check .` and `uv run ruff format .` check and format by hand.
- `uv run lint-imports` checks by hand that each app imports only from the
  floors below its own; the tests run it too
  ([ADR-0007](docs/adr/0007-apps-in-layers.md)).
- `uv audit --preview-features audit-command` checks every package in
  `uv.lock` for known security issues.
- CI runs all of these on GitHub, plus a secret scan, on every push to `main`
  and every pull request ([ADR-0006](docs/adr/0006-ci-on-github-actions.md)).
- `/health/` answers 200 when the site and its database work, 503 when the
  database does not answer.

## Documentation

- [Plan](docs/PLAN.md): what is built, in what order, and where we are
- [Modules](docs/MODULES.md): what the system does, part by part
- [Architecture](docs/ARCHITECTURE.md): how the code is organised
- [Design](docs/DESIGN.md): how screens look and behave
- [Glossary](docs/GLOSSARY.md): the one name for each thing
- [Decisions](docs/adr/README.md): why
- [Contributing](CONTRIBUTING.md): how work is done

## License

Proprietary. All rights reserved. The source code is published for viewing
only. See [LICENSE](LICENSE).
