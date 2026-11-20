# Architecture

How the code is organised. What is planned: `docs/PLAN.md`. Why: `docs/adr/`.

The layers and the inside of every app are decided (ADR-0007). The list of
apps is a plan: each app's place is checked again when it is built, and an
open decision below gets its ADR first.

---

## What we optimise for

- **Availability is always right.** Nobody can promise pieces that are
  out, booked or missing. This is the client's first rule.
- **Correct money.** Every rupee traceable to the record that moved it.
- **Safe for many businesses.** No data can cross from one business to
  another (ADR-0012).
- **Nothing lost.** A record is never deleted; a cancelled or changed one is
  kept and marked.
- **Easy to change.** Every rule has one home, so anyone can say which file
  to change when a rule changes.
- **Simple to run.** One application and one database per deployment.

## Deployment model

One repository and one codebase, on every server (ADR-0012):
- **dedicated:** one business on its own server;
- **shared:** many businesses on one server, each seeing only its own data.

What differs between servers is configuration (environment variables), and
between businesses their own settings, never code.

## Project layout

```
rentalos/
├── apps/              all Django apps (below)
├── config/            settings (base, local, test), urls, wsgi, health check
├── tests/             project-wide tests (settings, safe defaults, layers, keys)
├── docs/
├── .github/           CI and the pull request template
├── pyproject.toml     dependencies, ruff, import-linter and pytest settings
├── uv.lock            exact versions of every dependency
└── manage.py, README.md, CLAUDE.md, CONTRIBUTING.md, LICENSE, .env.example,
    .pre-commit-config.yaml
```

Each comes with the step that first needs it (`docs/PLAN.md`):
`templates/` (base layouts, shared components, state pages), `static/`
(design system CSS, icons, shared JS, htmx), `locale/` (Malayalam, when
wanted), `design/lab/` (UI lab pages, never imported by the app), and
`config/settings/production.py`.

## Apps: small, each answering one question

| App | Holds | Built in |
|---|---|---|
| `core` | shared tools: the base model that gives every model its UUID7 key (ADR-0008); later money, Indian formats, template helpers. No business rules | step 0 |
| `users` | users, and later their roles and sign-in | step 0 (the user) |
| `businesses` | the business, its branches and godowns; the base of every business record | step 1 |
| `stock` | items, categories, item photos, how many pieces each item has | step 3 |
| `customers` | event companies and direct parties | step 4 |
| `bookings` | estimates, follow-ups, bookings with their event details, borrowed items | step 4 |
| `godown` | the Loading Sheet, Out, the return check, the Missing & Damage list, Recovered | step 5 |
| `bills` | extra charges, the final bill, the discount, the round-off, payments, the balance | step 6 |
| `reports` | the owner dashboard, if one is wanted; read-only | to decide |
| `staff` | staff, their work on bookings, attendance, wages (Release 2) | step 9 |

An app is created with its first real code: a model, a page or a shared
tool. No empty apps.

## Layers: who may import whom

```
Top        reports                   (nothing imports it)
Business   bills
           godown, staff
           bookings
           stock, customers
Base       users
           businesses
           core
```

- An app may import only from apps in **lower rows**, never the same row,
  never above.
- **Model links follow the same rule.** A model links only to its own app's
  models or to lower rows. A link written as text
  (`ForeignKey("bookings.Booking")`) needs no import, so import-linter cannot
  see it; a test does.
- A lower app never reads an upper one. When it needs data that an upper app
  creates, the upper app's service passes it down.
- `staff` sits above `bookings`, because staff are given work on a booking.
  Release 2 then adds its app without changing Release 1.
- The row order lives in the `import-linter` settings in `pyproject.toml`,
  so it has one home. `tests/test_layers.py` runs import-linter and checks
  every model link against the same rows. A new app is placed there in the
  same commit.

## Inside every app: the same files every time

```
bookings/
├── models.py      the data
├── services.py    rules that CHANGE data (hold pieces, cancel, convert)
├── selectors.py   rules that READ data (lists, totals, availability)
├── forms.py       checks what was typed
├── views.py       thin: request, then form, then service, then response
├── urls.py
├── admin.py       only for the setup records allowed in the admin
├── templates/bookings/
├── static/bookings/
└── tests/
```

| You are writing | It goes in |
|---|---|
| a database table | `models.py` |
| anything that creates, changes or cancels data | `services.py` |
| a query for a list, a total or availability | `selectors.py` |
| a check on what a person typed | `forms.py` |
| the handling of a page request | `views.py`, kept thin |
| a page address | `urls.py` |
| HTML | `templates/<app>/` |
| page-specific CSS or JS | `static/<app>/` |
| a component used by several pages | `templates/components/` and `static/` |
| a rule used by many apps (money, dates) | `core` |
| a test | `<app>/tests/` |

- **No business logic in signals.** Every change happens through an explicit
  service call.
- **No CSS or JS inside templates.** It lives in static files, which allows a
  strict Content-Security-Policy.

---

## Shared rules

- **Dates:** India time, `timezone.localdate()`, never `date.today()`.
- **Money:** `Decimal` only, never `float`. One money column and one box for
  every amount come with step 1.
- **Nothing is deleted:** a cancelled or changed record is kept and marked.
- **History:** record when things happen. A status change that matters
  (booked, out, returned, recovered, billed, paid) keeps its time, as rows,
  one per change, never only the latest. Reports and Release 2 build on this
  history, and it cannot be filled in later.
- **Changes that decide a count or money** run in one transaction and lock
  the rows they read (`CONTRIBUTING.md`, Code rules).
- **Safe defaults** (`config/settings/base.py`): every page needs sign-in,
  unless marked `@login_not_required`; a page shown to a signed-in person is
  never kept by the browser (`apps/users/middleware.py`); a strict
  Content-Security-Policy, with no inline script or style.

---

## Open decisions: each becomes an ADR

1. **The business base** (step 1): how ADR-0012 is built. Proposal: every record links to its
   business, and most also to a branch; PostgreSQL refuses a link to another
   business's record; the business is passed by hand to every query, never
   kept as a hidden "current business". Users see no branch or godown until
   a second one exists.
2. **Sign-in and roles** (step 1): how each of the four roles signs in, how
   long a session lasts, and how a page says what it needs, so no page checks
   a role by its name.
3. **Hosting** (step 2): which host, whose account, backups and the
   address.
4. **Item photos** (step 3): where uploaded photos are kept on the server,
   and the image library.
5. **Availability** (step 4). Proposal: the rows that make a piece
   unavailable (held by a booking, out, missing) live in one low app,
   written by the services of the apps above it, so one selector reads them
   all. To settle: which dates a booking holds its pieces for, and how two
   bookings saved at one moment meet at a lock.
6. **The Loading Sheet** (step 5): a print page from the browser, or a PDF
   made on the server.
7. **Change history** (step 6): whether a change to money keeps a frozen
   copy of what changed, who and when.
8. **Per-business settings** (with the first one): each setting lives
   beside the rule that uses it, in its app, one row per business; with no
   saved row, the default in the code applies. A setting acts at the moment
   of an action, never on saved records.
