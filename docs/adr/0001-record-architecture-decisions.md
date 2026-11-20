# 0001: Record architecture decisions

**Status:** Accepted (2026-11-20)

## Context

A decision made in a chat, or kept inside one long instruction file, is hard
to find later. When someone reverses it, the earlier reasoning is not
visible.

## Decision

Every significant decision gets a short ADR in `docs/adr/`, in the format set
out in `docs/adr/README.md`. Accepted ADRs are not rewritten; a new ADR
supersedes an old one.

## Consequences

- Anyone, a new developer or a new AI session, can find why something is
  the way it is.
- A small extra effort for each decision.
