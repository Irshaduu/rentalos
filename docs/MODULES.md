# Modules

What the system does, part by part, and when each part is built.
Order of work: `docs/PLAN.md`. Words: `docs/GLOSSARY.md`. Each part's rules:
`docs/rules/<part>.md`, written when its building starts.

---

## The business

The client rents out event serving equipment (counters, serving vessels,
cloths and premium showpieces) from one godown. Most bookings come from
other event management companies; sometimes a party books directly. The
team also sets the items up at the venue, and can supply service staff. The
business earns rent for the items, extra charges (transport, loading and
unloading, washing, setup and service staff), and the purchase price of any
piece that comes back broken or never comes back.

**The client's own rules for the system**
1. **Availability is always right.** Nobody can promise pieces that are
   already out or booked.
2. **Stable.** No surprises, no lost data, no "the system is down" in the
   busy season.
3. **Easy for every user**, from the owner to the godown manager: simple
   screens, few steps, no training manual.
4. **No complications.** Late payments, missing pieces coming back and a rare
   borrowed item are handled simply, without extra parts.

**When:**
- **Release 1:** built now; each part goes live as soon as it is built and
  checked
- **Release 2:** after Release 1 is stable
- **Later:** ready in the structure, switched on when needed

---

## Release 1

| Part | What it does | App |
|---|---|---|
| Users and roles | Four roles sign in: Owner (sees and does everything), Accountant (final bills, extra charges, discounts, round-off, payments, balances), Office Staff (customers, estimates, follow-ups, bookings, sending the Missing & Damage bill), Godown Manager (stock, without purchase prices (point 2 below), delivery, the return check, the Missing & Damage list). Users are not staff | `users` |
| Business, branch and godown | One business, one branch, one godown today. Nobody sees them until a second godown or branch exists | `businesses` |
| Stock | Items with a photo, name, category, stock, purchase price and rent. Four categories: Counters, Serving Vessels, Cloths, Premium | `stock` |
| Availability | How many pieces of each item are available on a date: not booked, not out, not missing. A missing piece is not available; once recovered it is available again; once charged it leaves the stock | to decide (`docs/ARCHITECTURE.md`) |
| Customers | Event companies and direct parties, added once and picked after | `customers` |
| Estimates and follow-ups | The price offer, with the rent from the stock list and what is available on the date; reminders to call the customer back. Estimates go out at the normal rent | `bookings` |
| Bookings | An estimate becomes a booking, edited if anything changed. The booking holds its pieces for its date, and keeps the event details: event date, venue, setup date and time, site manager, service staff needed | `bookings` |
| Godown out and return | The Loading Sheet, printed in clear black and white; Out in one step; the return check in the sheet's order; the Missing & Damage list and its bill; Recovered | `godown` |
| Accounts and bills | Extra charges (one typed total each), the discount (only the Accountant or the Owner), the round-off, the final bill, payments in any pattern, the balance | `bills` |
| Borrowed items | Lines on a booking for an item taken from another event group: not stock and no effect on availability, but on the delivery and return lists, and on the bill with their cost to us | `bookings` |

## One booking, start to finish

1. Office Staff add the customer, or pick one who exists.
2. Office Staff make an estimate. The system shows what is available on that date.
3. Follow-ups until the customer decides.
4. The estimate becomes a booking, edited if needed. Its pieces are now held
   for that date.
5. The Accountant records an advance, if one is paid.
6. The Godown Manager prints the Loading Sheet and ticks each item on paper
   while loading.
7. The Godown Manager marks the booking Out, in one step, correcting any
   line that loaded short.
8. The sheet goes with the site manager. The team sets up at the venue; the
   event happens; service staff work there if booked.
9. The items come back. The Godown Manager counts everything again: the
   return check.
10. The site manager checks by hand against the same sheet.
11. The Godown Manager checks any difference again and saves the final count.
12. The Godown Manager makes the Missing & Damage list and its bill.
13. Office Staff send that list and bill to the customer.
14. A piece brought back, or collected by our staff, is marked Recovered and
    taken off the bill.
15. The Accountant adds the extra charges.
16. The final bill: rent, plus extra charges, plus missing and damage, minus
    the discount, plus or minus the round-off.
17. Payments, in any pattern, until the balance is 0.

---

## Release 2

| Part | What it does | App |
|---|---|---|
| Staff and salary | Staff by type (monthly salary, daily wage, temporary); staff given work on a booking (site manager, setup crew, service boys), matched against the service staff needed; attendance; wages, salaries, advances and payments; the real profit of each booking | `staff` |

**Release 1 is ready for it,** so nothing from Release 1 is changed or typed
again:
- The booking is the centre of everything, with its event details and the
  service staff needed.
- Users and staff are separate. A user can later be linked to a staff
  record.
- Every booking can carry costs, not just income. Borrowed items already do.
- The service staff charge is a bill line from day one.
- Everything belongs to a branch, staff included.
- Nothing is ever deleted: cancelled or changed records are kept and marked.

## Later

| Part | What it does | App |
|---|---|---|
| GST bills | A bill can become a GST bill when the business needs one. Tally stays with the accountant: no accounting is rebuilt | `bills` |
| More godowns and branches | A second godown, with stock seen together and items moved between them; a separate branch with its own godowns, stock and accounts. A place that must share nothing is a separate business (ADR-0012) | `businesses` |
| SaaS business features | Other rental businesses use the system as a paid service: sign-up, subscription billing, a platform admin panel, module switches. Only when a second business wants it (ADR-0012) | to decide |

---

## Points to settle, with the default we use

None of these blocks the work. Each has a default, used unless the client
says otherwise, and is confirmed in its part's rules.

| # | Point | Default |
|---|---|---|
| 1 | Are missing pieces charged at the purchase price, the same as broken ones? | Yes, the same rule |
| 2 | Can Office Staff and the Godown Manager see purchase prices? | Only the Owner and the Accountant see them. The godown sees only the damage charge on its list |
| 3 | Does an event over several days still pay rent once? | Yes, once per booking |
| 4 | Is a printed or shared delivery note needed when items go out? | A simple delivery list, printable and shareable |
| 5 | Will the field marketing team use phones for customers and estimates? | Yes: the sales screens work well on phones |
| 6 | Are premium items counted, or followed piece by piece? | Counted, like other items |
| 7 | The owner dashboard, and WhatsApp sharing of estimates and bills, in Release 1? | Decided in the plan; both are cheap to add |
| 8 | Monthly-salary and fixed staff: one group or two? | Release 2 only |
| 9 | A future separate branch: shared customers? Does the owner see all branches together? | Future only |
| 10 | Are setup and service staff charged apart on the bill, or included in the rent? | Separate optional lines, left empty if included |
| 11 | If more items are sent later on a second trip? | A small extra Loading Sheet for just those items |
