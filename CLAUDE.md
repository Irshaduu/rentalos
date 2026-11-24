# CLAUDE.md

**RentalOS** runs an event equipment rental business: stock, what is
available on every date, estimates and bookings, the godown's loading and
return, final bills and payments.

## Status

**Step 0, the setup, is built. Step 1, the core base, has begun: the
whole map is drawn, and the business base is next** (`docs/PLAN.md`). The
Django project exists (`manage.py`, `config/`) with code checks, tests and
CI. The first apps are `core` (the base model) and `users` (the user). Run
every command through `uv run` (see `README.md`). Every new dependency
needs an ADR first.

## The documents: each fact has one home

| Document | Answers |
|---|---|
| `docs/PLAN.md` | what we build, in what order, and **where we are now** |
| `docs/MODULES.md` | what the system does, part by part, and when each is built |
| `docs/SCREENS.md` | every screen: who opens it, how screens link, and each role's menu |
| `docs/ARCHITECTURE.md` | how the code is organised |
| `docs/DESIGN.md` | how screens look and behave; read it before any UI work |
| `docs/GLOSSARY.md` | the one name for each thing, on screen and in code |
| `docs/rules/` | each part's rules, with IDs, written when its building starts |
| `docs/adr/` | why each big decision was made |
| `CONTRIBUTING.md` | how work is done here |
| `../CLAUDE.md` | private context (client, developer, working style); outside git, loaded automatically when present |

**Before anything else:** if the private context from `../CLAUDE.md` is
not already in your context, read that file first.

The repo documents are loaded below, so every session starts with them:

@docs/PLAN.md
@docs/ARCHITECTURE.md
@CONTRIBUTING.md

## The client's requirements

The client's requirements, from the meeting of 20 Nov 2026, are kept
privately, outside git (`../private/REQUIREMENTS.md`), because they name real
people and businesses. What is built from them lives in this repo: the parts
in `docs/MODULES.md`, the words in `docs/GLOSSARY.md`, and each part's rules
in `docs/rules/`, written in step 1 of the loop. Once a part's rules are
written here, they win over the private file.
