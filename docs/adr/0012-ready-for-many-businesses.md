# 0012: One codebase, ready for many businesses and branches; SaaS features wait

**Status:** Proposed (2026-11-20)

## Context

- Today there is one business, one branch and one godown
  (`docs/MODULES.md`).
- Later, the client may add:
  - a second godown nearby, connected: stock seen together, items moved
    between them;
  - a separate branch far away, with its own godowns, stock and accounts,
    and maybe its own partners;
  - a place that shares nothing at all with the first.
- The developer may also give the system to other rental businesses, as a
  paid service (SaaS). Maybe; nothing is decided.
- Adding "which business does this record belong to?" after real bookings
  and money exist means changing every table and every query on live data:
  the riskiest kind of change. Adding it with the first business record
  costs little, and the developer's earlier project has tested code for it.
- SaaS business features (sign-up, subscription billing, a platform admin
  panel, turning parts on or off per business) take real time, and are
  wasted if no second business ever comes.

## Decision

- **One codebase for every business and every server.** Never a copied
  codebase. What differs between servers is configuration; what differs
  between businesses is their own settings.
- **Three levels: Business, then Branch, then Godown** (`docs/GLOSSARY.md`):
  - connected places are godowns of one branch: stock seen together, items
    moved between them;
  - a separate branch has its own godowns, stock and accounts; its users see
    only their branch, and the owner sees every branch;
  - a place that must share nothing is a second business, with its own
    records, users and numbers. Another rental business is the same case.
- **A second place is a branch by default.** It becomes a second business
  only when a wall is truly needed, by law or by choice: for example,
  partners who must not see each other's data.
- **Built in step 1, before any business record** (`docs/PLAN.md`): every
  business record belongs to one business, and most also to a branch; a
  query never mixes two businesses, and a test proves it for every model.
  Nobody sees a branch or a godown until a second one exists.
- **A business runs on its own server or on a shared one,** with the same
  code.
- **SaaS business features wait** until a second business wants the system:
  sign-up pages, subscription billing, a platform admin panel, module
  switches.

## Consequences

- A second godown, branch or business is set up, never rebuilt.
- Every model and query carries its business, and most also their branch,
  from the start: a small, steady cost, guarded by tests.
- Nothing is built for selling until it is needed. If no second business
  ever comes, the only cost is the business link.
- Before a second business shares a database, a second guard is added:
  PostgreSQL row-level security.
