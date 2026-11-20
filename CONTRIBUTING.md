# Contributing

How work is done here.
What is planned: `docs/PLAN.md`. Structure: `docs/ARCHITECTURE.md`. Why: `docs/adr/`.

`ruff`, `pre-commit` and `pytest` are set up (ADR-0005), and CI runs every
check on GitHub (ADR-0006). **`main` is protected:** every change reaches it
through a pull request, and only when CI is green.

---

## The flow

1. A **branch**: `feat/<short-name>`, `fix/...`, `docs/...`, `refactor/...`,
   `chore/...`. Never a commit on `main`.
2. **Small commits**, each with its tests.
3. A **pull request** into `main`. Its template says why and what changed,
   and carries the definition of done.
4. **Rebase and merge**: GitHub merges by itself when all four CI checks
   pass (auto-merge). Each commit lands on `main` with its own checked
   message, in a straight line, and the branch is deleted.
5. On the laptop: `git switch main`, then `git pull`.

An **issue** is only for work that has to wait: a bug found, or a client
request for later. The pull request that does it says `Fixes #N`, which
closes the issue.

## Commit messages

[Conventional Commits](https://www.conventionalcommits.org/):
`type(scope): summary`, for example `feat(bookings): hold the pieces of a booking`

- Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`
- Summary: present tense, 72 characters or fewer
- Body: **why**, not what. The diff already shows what.

---

## Building a part: the loop

A part is one row of `docs/MODULES.md`, like Stock or Bookings.

1. **Rules:** list the part's rules into `docs/rules/<part>.md`, each with an
   ID, from the client's requirements and later answers; its words go into
   `docs/GLOSSARY.md`. A point the client has not settled is written with its
   default, marked to confirm.
2. **Design:** a main screen (one a role uses all day, like availability,
   the booking or the return check) gets one design in the UI lab first.
   Other screens are built straight from the components.
3. **Plan:** a short written plan: models, screens, tests. Approved before
   code.
4. **Build:** small commits on a branch, tests in the same commit.
5. **Check:** CI green; clicked through in a browser at phone, tablet and
   laptop widths; behaviour matches the rules.
6. **Merge:** rule catalogue updated; an ADR if a decision was made.
7. **Sign-off:** the client checks it on staging before it goes live.

## UI lab

- Lives in `design/lab/<part>/`. **Never imported by the app.**
- Uses the real design tokens and fake data, and follows `docs/DESIGN.md`.
- The design system is the first lab page, `design/lab/system/`: every
  token and component in every state, the reference to check before writing
  a screen (ADR-0010). It stays.
- A main screen gets one proposed design, with the reason it is recommended.
  A second design only when the developer asks for one; then one is chosen,
  or parts of both are combined.
- When the screen is built, its lab page is deleted. One screenshot and one
  line of reasoning stay in `docs/design/`.
- A small choice (one colour, one space) gets one version, changed if
  needed.

---

## Code rules

- **One implementation per rule.** Search before writing anything new.
- **One name per thing** (`docs/GLOSSARY.md`). The word on screen is the
  name in models, functions, files, addresses and docs. A new word goes in
  the glossary first.
- **Extract on the second use**, never before. No abstraction for one caller.
- **Code goes where `docs/ARCHITECTURE.md` says.** Views thin; rules in
  `services.py` (changes) and `selectors.py` (reads).
- **An app imports, and links its models, only to lower layers**
  (ADR-0007). A new app is placed on its floor in `pyproject.toml` in the
  same commit. No generic links (`GenericForeignKey`): PostgreSQL cannot
  guard them. Tests check all three (`tests/test_layers.py`).
- **Every model builds on `core`'s base model** (`apps/core/models.py`), so
  its key is a UUID7 that exists before saving (ADR-0008). To know if a
  record is saved, ask Django's `_state.adding`, never "is the key empty?".
  A test checks every model.
- **Every page needs sign-in.** A public page is marked
  `@login_not_required`, with a comment saying why.
- **A business record is never deleted.** A cancelled or changed record is
  kept and marked, so past bookings and bills stay true, and staff and wages
  can be added to them later (`docs/MODULES.md`).
- **Money is `Decimal`, never `float`.** Dates use `timezone.localdate()`;
  ruff stops `date.today()` and `datetime.now()`.
- **A service that changes stock, the pieces a booking holds, or money runs
  in one transaction** and locks the rows it reads to decide
  (`transaction.atomic`, `select_for_update`). Two bookings saved at the same
  moment must never take the same pieces.
- **A locking query joins nothing:** no `select_for_update()` with
  `select_related()`. A save that waited for the lock would get the row as it
  is now beside the linked row as it was. Read the links after the lock.
- **A balance, a total or what is available is worked out from its rows
  when it is read.** It is stored only when measured slowness needs it, with a test that
  it equals its rows.
- **A calculation rounds on purpose before it saves.** PostgreSQL rounds an
  extra decimal with no error.
- **A box for a number is a text box with `inputmode`, never
  `type="number"`:** the mouse wheel can change a number box, and it sends an
  empty value for `2,950`. pre-commit reads every template.
- **Every text a person sees is marked for translation** (ADR-0009):
  `{% translate %}` in templates, `gettext_lazy` in Python.
- **No business logic in signals.** Every change happens through an explicit
  service call.
- **Business records are never in the Django admin.** It holds only the
  setup records listed in `tests/test_safe_defaults.py`, for emergencies. A
  business record changes only through its service, so every rule runs. The
  test fails for any other model.
- **Let PostgreSQL 18 guard the data** (ADR-0004). Before writing a model or
  a query, check what PostgreSQL 18 and Django can do in the database:
  constraints (unique, check, exclusion), generated fields, database
  defaults. Use one when it makes the data safer or the code simpler. Write
  it through Django in `models.py`, never as a trigger or a stored
  procedure, so the flow stays visible.
- **No CSS or JS inside templates**: no `style` attribute, inline `<script>`
  or `onclick` in any HTML; scripts come from static files. pre-commit
  checks it.
- **A colour is written only in `static/css/tokens.css`.** Every other file
  uses its token (ADR-0010). pre-commit checks it.
- **A size in px or rem is written only in `static/css/tokens.css`**
  (ADR-0010), except 1px and 2px lines and media query widths. pre-commit
  checks it outside `design/lab/`.
- **The server decides; JavaScript only shows** (ADR-0011). htmx 4 for
  server calls: mark inherited attributes with `:inherited`, use the htmx 4
  event names, and no `hx-on`, `js:` values or trigger filters. JS modules
  hold no business rules and work out no money or availability.
- **Delete code; never comment it out.** Git remembers.
- **No dead files, no experiments on `main`.**
- **Every new dependency needs an ADR.**

## Tests

- **Every rule has a test**, named after the rule it protects, and linked to
  its rule ID.
- **Test the invariant, not the implementation.** For example, the available
  pieces of an item never go below zero, or a balance adds up from its
  payments.
- **A rule is tested at its service or selector.** A page test checks only
  the page's wiring and who may open it.
- **A count that two people can change at once is also tested at once:** two
  saves at the same moment meet at a lock, and the count is never wrong.
- **`transaction=True` only when a test needs a real commit.** It empties
  every table after each test, so it is slow.
- **Factories, not hand-made fixtures.**
- **Browser tests** for the key flows, before Release 1 closes.
- **A failing test means the code regressed.** Fix the code, not the test.

## Docs

- **One fact, one home.** Link; never repeat.
- **A plan task is one line, in the step that does it.** Its detail lives
  in its home doc.
- **No hand-written counts.** Generate them or leave them out.
- **Docs say what is true now.** History lives in git and in ADRs.
- **An ADR for every decision that is hard to undo.** The format is in
  `docs/adr/README.md`.
- **Re-check a plan when its building starts.** An ADR, plan task or design
  written earlier is checked again against what changed since and against
  the whole system: is there now a simpler, safer or more stable way? The
  check fits the item: one line for a small task, full pros and cons for an
  ADR, a design or a rule. It ends in a decision: keep, change or drop. A
  Proposed ADR is edited; an Accepted one is replaced by a new ADR. Scope
  can wait; quality never does.
- **Plain, natural English** in docs, screens and commit messages. Short
  sentences, everyday words, no em dashes, arrows or decorative symbols.
  pre-commit checks it.
- **Written so another developer could take over.**
- **No client names, customer data or personal details anywhere in the
  repo.** A test phone number is plainly fake, like 9000000001.

---

## Definition of done

The checklist lives in the pull request template
(`.github/pull_request_template.md`), so every pull request carries it.

## Never commit

- `.env` or any secret
- Real customer data, the client's own photos, database dumps, backups
- Logs, build output, caches
