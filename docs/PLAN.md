# Plan

What we build, in what order, and where we are.
How we work: `CONTRIBUTING.md`. Structure: `docs/ARCHITECTURE.md`.
Parts: `docs/MODULES.md`. Design: `docs/DESIGN.md`. Why: `docs/adr/`.

**Now:** step 1, the core base. The whole map is drawn; the business base
is next.
**Alongside:** the written agreement with the client, needed before go-live,
not before code.

Marks: `[x]` done, `[~]` in progress, `[ ]` to do

---

## Goal

- A rental system for one business: stock, what is available on every
  date, estimates and bookings, the godown's loading and return, final bills and
  payments (`docs/MODULES.md`, Release 1).
- Live for the client's busy season, December and January, one part at a
  time, the most painful first.
- Ready for more godowns, branches and businesses later, without rebuilding.
- Built in small, reviewed, tested steps.

## Decided

- **One codebase, ready for many businesses and branches** (ADR-0012). A
  second godown, branch or business is set up, never rebuilt. SaaS business
  features wait until a second business wants the system.
- **Release 1 now, Release 2 (staff and salary) after Release 1 is stable.**
  Release 1 is already ready for Release 2 (`docs/MODULES.md`).
- **Each part goes live as soon as it is built and checked**, not all at the
  end. The client's notebook runs alongside for the first weeks.
- **The whole map first, in low detail:** every screen
  (`docs/SCREENS.md`), the booking's journey (`docs/MODULES.md`), who may
  do what (`docs/rules/roles.md`) and the data map
  (`docs/ARCHITECTURE.md`). So the base is built for all of it, and each
  part adds its own detail in its loop.
- **Each part's screens are designed one part ahead of their code:** while
  steps 1 to 3 are built, step 4's screens. The developer approves each
  design. The people who will use a part try it on staging before it goes
  live, which is also their training.
- **Dates come from measured time.** Each step's hours are recorded
  (privately, per branch) and size the next steps. No date is given from a
  guess.
- **Go live early.** The hosting, backups and error tracking come right
  after the core base, so every later part goes live the day it is ready.
- **The most-used items are entered first.** The rest of the stock follows.
- **Quality never waits for the deadline.** Scope can wait; correctness,
  edge cases and tests never do.
- **No accounting is rebuilt.** Tally stays with the accountant; GST bills
  come later, when the business needs them.
- **The written agreement is needed before go-live.** Code does not wait for
  it.

## Lessons we start with

From the developer's earlier projects:

| What went wrong before | Rule now |
|---|---|
| Building began with no plan, part list or screen design | Plan, part list and the main screens designed before code |
| Everything was built before anything went live | Each part goes live when it is built and checked |
| Work began before a written agreement | The agreement before go-live |
| Changes merged with no review step | Every change reviewed before merge |
| Tests run by hand, sometimes only part of them | CI runs every check on every pull request |
| No JavaScript ever ran under test | Browser tests for the key flows |
| One rule copied into many screens | One implementation per rule |
| CSS and JS written inside templates | Static files, a design system, a strict CSP |
| Code assumed one business | Ready for more godowns, branches and businesses from the first model |
| Stock moved through signals, an invisible flow | Explicit service calls; no business logic in signals |
| A service worker re-sent form POSTs, which some browsers dropped | A save is never sent again by itself |
| One thing had two names | One name per thing (`docs/GLOSSARY.md`) |
| Back, after signing out on a shared laptop, showed a bill again | A signed-in page is never kept by the browser |
| Client names and a phone number inside the repo | No real people or data in the repo |
| Deploy settings lived only in the hosting dashboard | Everything about deploying lives in the repo |

---

## Steps

Each step goes through the loop in `CONTRIBUTING.md`, in one or more pull
requests. Base work gets its own pull request, just before the page that
first uses it.

| # | Step | Status |
|---|---|---|
| 0 | Setup | `[x]` |
| 1 | Core base | `[~]` |
| 2 | Live early | `[ ]` |
| 3 | Stock | `[ ]` |
| 4 | Availability and bookings | `[ ]` |
| 5 | Godown out and return | `[ ]` |
| 6 | Accounts and bills | `[ ]` |
| 7 | Borrowed items | `[ ]` |
| 8 | Close Release 1 | `[ ]` |
| 9 | Release 2: staff and salary | `[ ]` |
| Later | SaaS business features | `[ ]` |

### Alongside: the client

- [ ] The written agreement, before go-live (kept privately, outside this
      repo)
- [ ] The points to settle in `docs/MODULES.md`, each confirmed or left at
      its default
- [ ] The list of the most-used items, with their photos, from the client
- [ ] The logo and the details printed on the Loading Sheet and the bills
- [x] The devices: an iPhone, an Android phone, a tablet and a Windows
      laptop (`docs/DESIGN.md`). The printer is point 22 in
      `docs/MODULES.md`

### Alongside: running it, from the first part live

- [ ] Releases at a quiet time agreed with the client, never during loading
      or an event
- [ ] An incident plan: what to do when the system is down, and who to
      tell; the client's notebook is the fallback
- [ ] Short training for each role, when its first part goes live
- [ ] Monthly: a test restore, a cost check, and dependency updates. Each
      update takes an exact version that has been out for at least a week,
      uv and the Python version in `.python-version` included. The release
      notes of Django, PostgreSQL and psycopg are read too, because
      `uv audit` can miss a security fix
- [ ] Client feedback becomes issues

### Step 0: Setup

- [x] Python 3.14 with uv (ADR-0002), Django 6.1 (ADR-0003), PostgreSQL 18
      (ADR-0004)
- [x] Code checks and tests: ruff, pre-commit, pytest-django (ADR-0005)
- [x] CI: code checks, tests, missing migrations, dependency audit, secret
      scan (ADR-0006); the health check
- [x] Apps in layers, checked by the tests (ADR-0007); UUID7 keys (ADR-0008)
- [x] Safe defaults: every page needs sign-in, a strict CSP, a signed-in page
      is never kept by the browser, a small admin
- [x] The user model, before any other app's first migration
- [x] Translatable text from the first app (ADR-0009)
- [x] The pull request template with the definition of done
- [x] The repository on GitHub, public; `main` pushed and protected: the
      four checks, rebase only, auto-merge, push protection (ADR-0006)

### Step 1: Core base

What every later part stands on. Each piece is re-checked for this client
before it is built, and brings its rules into `CONTRIBUTING.md` and its
tests in the same pull request.

- [x] The whole map, in low detail: every screen, the booking's journey,
      who may do what, the data map, the client's questions in one list,
      and availability by time (ADR-0013)
- [ ] The business, its branches and godowns, as ADR-0012 decides, with an
      ADR for how first: every record belongs to one business, most also to
      a branch; a link never
      crosses to another business's record; a test shows each business only
      its own records
- [ ] Users and roles, with an ADR first, from `docs/rules/roles.md`: the
      four roles, the sign-in page, a mark on every page naming what it
      needs, a test of every page for every role, with the answers typed by
      hand, and the Owner's Users screen
- [ ] The page base: the base layout, the state pages (`docs/DESIGN.md`),
      and the design system in `design/lab/system/`: tokens, components,
      icons (with their ADR), htmx (ADR-0011)
- [ ] Money: one column and one box for every amount
- [ ] Indian dates and numbers on screen, from one formats file
- [ ] A double tap or a weak signal never saves a record twice: the server
      is the guard; the button only shows it is busy
- [ ] A save changes only what the person changed, so two people working on
      one booking never undo each other's work
- [ ] A longer list never means more queries: a test for every page that
      shows rows
- [ ] JavaScript unit tests with Node's own test runner, with the first JS
      module (its ADR, and a step in CI)

### Step 2: Live early

- [ ] Hosting decided with the client: which host, whose account, the
      address
- [ ] Production settings, and everything about deploying, in the repo;
      migrations run before traffic moves
- [ ] Staging (fake data) and production; `main` goes to staging, a release
      tag goes to production
- [ ] Automatic backups, an off-site copy, a test restore
- [ ] Error tracking and an uptime monitor; logs never hold customer data
- [ ] The production mailer, if sign-in needs mail
- [ ] Static files with hashed names and compressed pages, served by the app
      (an ADR)
- [ ] Safe-migration rules written down, before the first real data
- [ ] A security pass: `manage.py check --deploy` clean in CI, the admin
      locked down, two-factor sign-in for the superuser, a review against the
      OWASP Top 10
- [ ] `RUNBOOK.md`: deploy, roll back, restore a backup; a rollback tried on
      staging
- [ ] `CHANGELOG.md`, with release notes in plain words, from the first
      release tag

### Step 3: Stock

- [ ] Items and categories, with photos (the photo storage decided in an
      ADR first)

### Step 4: Availability and bookings

- [ ] Availability, with an ADR first (`docs/ARCHITECTURE.md`, open
      decisions)
- [ ] Customers, estimates and follow-ups
- [ ] Bookings: an estimate becomes a booking, which holds its pieces
- [ ] The go-live position, before the client relies on availability: the
      stock he owns, the pieces out now, and every booking already promised
      for a future date

### Step 5: Godown out and return

- [ ] The Loading Sheet, Out, the return check, the Missing & Damage list
      and bill, Recovered

### Step 6: Accounts and bills

- [ ] Extra charges, the discount, the round-off, the final bill, payments,
      the balance

### Step 7: Borrowed items

- [ ] Borrowed item lines on a booking, on the lists and the bill

### Step 8: Close Release 1

- [ ] Browser tests for the key flows (with their ADR): sign in, make a
      booking, return it, settle its bill
- [ ] The full test suite timed, with a time limit in CI
- [ ] The owner dashboard and WhatsApp sharing, if the client wants them in
      Release 1 (`docs/MODULES.md`, point 7)
- [ ] A page size limit, measured with a browser set to act like a slow
      phone, checked in CI
- [ ] Each part signed off by the client

### Step 9: Release 2: staff and salary

- [ ] Every row of Release 2 in `docs/MODULES.md`, through the loop

### Later: SaaS business features (ADR-0012)

- [ ] Only when a second business wants the system: sign-up, subscription
      billing, a platform admin panel, module switches
- [ ] PostgreSQL row-level security as a second guard, before a second
      business's data shares a database
