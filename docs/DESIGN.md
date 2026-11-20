# Design

How screens look and behave. Read it before any UI work.
What is planned: `docs/PLAN.md`. How the UI lab works: `CONTRIBUTING.md`.
Words on screen: `docs/GLOSSARY.md`.

CSS base: plain CSS with our own tokens, no framework (ADR-0010). The design
system (tokens, components, icons and their lab page, `design/lab/system/`)
is built in step 1 (`docs/PLAN.md`). It starts from the developer's earlier
project, whose components were measured for contrast and tap size, then
recoloured and fixed for this system.

---

## Design principles

The client's own rules come first (`docs/MODULES.md`): easy for every user,
and no complications.

- **One main thing per screen.** The most important number is the biggest
  thing on it. On an estimate or a booking, that is what is available on the
  date.
- **Colour means status, never decoration, and never alone.** Every status
  also has its word, because the Loading Sheet and bills print in black and
  white.
- **Few steps, little typing.** Where work is done standing up, like the
  return check: big photos, big numbers, very little typing.
- **Calm and fast.** Every effect must help the task; if it only decorates,
  it goes. Motion only with a purpose, and none when the device asks for less
  motion.
- **Measured, not guessed.** Each main screen is measured in the browser
  (no overflow, contrast, tap size) before it is called done.

## Devices and their users

| Who | Works on | To confirm with the client |
|---|---|---|
| Owner | phone | which phone |
| Accountant | laptop or phone | which device |
| Office Staff | laptop in the office; phones for the field marketing team | which devices |
| Godown Manager | phone or tablet, in a godown with a weak mobile signal | which device; the printer |
| Site manager | the printed Loading Sheet only (Release 1) | |

- Every screen works at phone, tablet and laptop widths.
- The sales screens work well on a phone (`docs/MODULES.md`, point 5).
- If anyone uses an iPhone, Safari's engine matters as well as Chrome's:
  every browser on an iPhone uses Safari's.

## Weak signal

- A save shows that it is working, and the button stays locked until the
  answer comes.
- A double tap or a slow network never saves the same thing twice. The server
  is the guard (step 1); the button only shows it is busy.
- With no internet, a save says "Not saved", and nothing is sent again later
  by itself.
- Pages stay light. A size limit is measured and set before Release 1 closes.

## Printing

- The Loading Sheet and the bills print clearly in black and white, in large
  type, on a plain printer. No colour printer is needed.
- What each print shows is in its part's rules (`docs/rules/`).

## Screen states

Each state is designed once, as a shared component, and every screen uses
it. A screen is not done until it handles every state that can happen on it.

| State | What the person sees |
|---|---|
| Loading | A loading sign. The save button stays locked until the answer comes. |
| Slow network | The same as loading. The server never saves the same thing twice. |
| Empty | That there is nothing here yet, and the next step (for example, add the first item). |
| No search results | That nothing matched the search, with a way to clear it. |
| Form errors | Each error next to its field, in plain words. What was typed stays. |
| Success | A short confirmation. |
| Server error | That something went wrong and nothing was saved, with a way to try again. |
| Not found | That the page or record does not exist. |
| Permission denied | That this role cannot open the page. None of its data is shown. |
| Session expired | The full sign-in page, never inside part of a page, saying what was not saved. |
| Offline | That there is no internet. A save says "Not saved", and nothing is sent again later by itself. |

## Numbers and dates

Indian numbers and dates on every screen, from one formats file (step 1),
read by Django's own filters. The rupee sign is written in the template,
before the number.

| Money | Looks like | Where |
|---|---|---|
| Whole rupees | 45,23,678 | A headline or a total, read at a glance |
| Paise when there are any | 1,200 or 499.50 | A list row, so it can be matched to its payment |
| Paise always | 17,800.00 | A printed estimate or bill, in a column a customer adds up by eye |

- An empty amount shows nothing, never 0.00 as if it were free.
- A money box holds a plain number with no commas, like 147500 or 1250.50,
  ready to type over. It is a text box with a number keypad
  (`inputmode="decimal"`), never `type="number"`.
- A count of pieces is a whole number, with a number keypad
  (`inputmode="numeric"`).

| Date | Looks like | Where |
|---|---|---|
| Date, the default | 3 Oct 2026 | Every screen, unless a line below says otherwise |
| Date and time | 3 Oct 2026, 3:05 PM | The "Printed on" line of the Loading Sheet, payments, in India time |

- A typed date is read day first: 10/11/2026 is 10 November.

## Help notes

A help note is a short line that explains how the system works. Once a
person knows the screen, it only gets in the way, so:

- **Behind the info button:** a note the person does not need to fill the
  form right or to make a decision. A tap shows it under its title; another
  tap hides it.
- **Always on the screen:** a warning before an action, a rule for what to
  type, an error, and a fact (a count, or how a figure is worked out).
- **How a note is written:** one or two short sentences in everyday words.

## Accessibility

The target is WCAG 2.2, level AA.

- Contrast: at least 4.5 to 1 for normal text, 3 to 1 for large text and
  for controls.
- Touch targets: at least 44 by 44 pixels. This is stricter than AA, which
  asks for 24.
- Labels: every field has a visible label. A screen reader hears a label on
  every box.
- Focus: a box that gets the keyboard focus is never hidden under a pinned
  header.
- Reflow: no sideways page scroll at 320 pixels wide. A wide table scrolls
  inside its own box.
- Checked: every lab page and every built screen at 320, 375, 768 and 1280
  pixels wide, by measurement and with the keyboard.
