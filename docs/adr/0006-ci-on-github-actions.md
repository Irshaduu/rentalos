# 0006: CI on GitHub Actions

**Status:** Accepted (2026-11-20)

## Context

- The pre-commit checks (ADR-0005) run only on a machine where they are
  installed, and a person can skip them on purpose. Something must check
  every change again, the same way, every time.
- The repository is public. A key or password pushed by mistake is public at
  once, and git history keeps it.
- The plan asks for these checks on every change: lint, tests, the
  missing-migration check, a dependency audit and a secret scan.
- On the free GitHub plan, only a public repository can protect `main`
  (checked 2026-11-20).
- Hosts and uptime monitors need one address that says whether the site
  works.

## Decision

- **GitHub Actions**, one workflow: `.github/workflows/ci.yml`. It runs on
  every push to `main` and on every pull request.
- **Four jobs**, run side by side, each a separate check:
  - **Code checks:** every pre-commit check on every file. The same commands
    as on the laptop.
  - **Tests:** a PostgreSQL 18 database in a container on GitHub's machine,
    then the missing-migration check (`makemigrations --check`), then pytest
    with a coverage report.
  - **Dependency audit:** `uv audit` checks every package in `uv.lock`
    against the OSV database of known security issues.
  - **Secret scan:** gitleaks scans every commit in the history for keys and
    passwords. Its output hides what it finds, because CI logs are public.
- **`main` is protected** by a GitHub ruleset: a change reaches it only
  through a pull request, by rebase, and only when all four checks pass;
  GitHub then merges by itself (auto-merge). No force push, and `main` cannot
  be deleted.
- **Push protection** is on: GitHub stops a known kind of secret before it is
  pushed.
- **Same versions as the laptop:** `uv sync --locked` installs Python and
  every package from `uv.lock`, and fails if `uv.lock` does not match
  `pyproject.toml`. The uv version is pinned in the workflow.
- **Every action is pinned to a full commit ID**, with its version in a
  comment. A version tag can be moved to other code; a commit ID cannot.
  gitleaks is downloaded at a fixed version and checked against its
  published checksum.
- **The workflow can only read the repository** (`permissions: contents:
  read`).
- **The CI environment** is the test settings, with values set in the
  workflow. Its secret key and database password are throwaway values that
  exist only in CI.
- **Health check:** `/health/` answers 200 with `{"status": "ok"}` when the
  database answers, and 503 with `{"status": "unavailable"}` when it does
  not. It is never cached. It lives in `config/`, because it belongs to the
  whole site, not to one app.

## Consequences

- Every push and pull request is checked the same way, and nobody has to
  remember to do it.
- No Docker on the laptop (ADR-0004). The database container runs only on
  GitHub's machine.
- `uv audit` is marked experimental in uv 0.13. Pinning uv keeps its
  behaviour fixed. If it changes or goes away, pip-audit does the same job.
- New security issues appear without any change to our code. The audit finds
  them only when CI runs.
- Push protection stops many secrets before the push; gitleaks finds the rest
  only after it. A pushed secret must be replaced, not just deleted.
- Pinned versions do not update themselves. The uv version, the action
  commit IDs and the gitleaks version are updated by hand, with the monthly
  dependency updates.
