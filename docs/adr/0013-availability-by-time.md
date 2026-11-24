# 0013: Availability by time: a booking holds its pieces from loading to back

**Status:** Proposed (2026-11-25)

## Context

- "Availability is always right" is the client's first rule
  (`docs/MODULES.md`). It fails both ways: pieces promised twice, or a
  shortage shown that is not real, which teaches the team to stop trusting
  the system.
- The busy season is December and January: many events, and the same
  pieces go from one event to the next.
- The approved design shows the trip of a booking's pieces with times:
  loading, the setup, the event, and back. Its hand-over lines (pieces that
  come back from one booking and go out to another) are worked out from
  the loading and back times.
- The design sample held pieces by whole days, from the day before the
  event to the day after: three days for a one-day event. So pieces back
  on a morning looked busy for a load leaving that afternoon.
- Plates and dishes often come back unwashed (the washing charge), and
  cloths need washing too, so some pieces may not be ready the moment they
  are back.
- A load not back yet keeps its pieces until they are counted (decided
  with the developer, to confirm with the client: `docs/MODULES.md`,
  point 14).

## Options

**A. By day:** a booking holds its pieces on whole days, from its loading
day to its back day.
- For: only dates to type. A day is free or not. Simple to work out and to
  test.
- Against: a one-day event holds three days. A load leaving the afternoon
  after another comes back shows as short when it is not. In the busy
  season that blocks real bookings, or sends the team to borrow items they
  do not need.

**B. By time:** a booking holds its pieces from its loading time to its
expected back time. A day shows its lowest count.
- For: it matches the real trip and the approved design. A same-day
  hand-over works. No day is lost on either side. Availability and the
  hand-over lines read the same times. It fits any rental business, even
  one with three events a day.
- Against: two more times on each booking, both filled from defaults. The
  count over a stretch of time is its busiest moment, a little harder to
  work out and to test. A load back later than expected can make a promise
  wrong, so a late load must show clearly, and stay held until it is
  counted.

## Decision

Option B.

- **A booking holds its pieces from its loading time to its expected back
  time.** Both are filled from defaults, and the office can change them:
  the loading 2 hours before the setup time; back at 11:00 AM the day
  after the last event day. The defaults are to confirm with the client
  (`docs/MODULES.md`, point 12).
- **A load not back by its expected back time stays held** until its
  return check saves the count, and shows as Not back yet.
- **Missing pieces stay held, with no end,** until they are recovered or
  charged.
- **The pieces available over a stretch of time** are the pieces owned,
  less the most that are held at any one moment in that stretch.
- **A day view** (the calendar, Availability, an item's next three weeks)
  shows each day's lowest count, so a day never looks freer than its
  busiest moment.
- **An estimate checks the pieces over its own trip.** Making it a
  booking checks again, under a lock.
- **If the client says some pieces need time after they are back**
  (washing cloths, for example), each category gets a time to be ready
  again, settled in step 4 (`docs/MODULES.md`, point 13).
- All times are India time.

## Consequences

- The booking gets a loading time and an expected back time, filled in
  from its setup time.
- A late load holds its pieces past its time, so the booking that waits
  for them shows the problem at once (the hand-over line, in red).
- No database constraint can say "the pieces held never pass the pieces
  owned": a constraint compares rows two at a time, and cannot add them
  up. The service checks it under a lock, as `CONTRIBUTING.md` says for
  every count.
- The tests cover a same-day hand-over, a late load, missing pieces, a day
  view, and two bookings saved at one moment.
- Step 4's availability ADR builds on this one: where the holds are kept,
  and how two saves meet at a lock (`docs/ARCHITECTURE.md`, open
  decision 5).
