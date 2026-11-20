# Glossary

One name for each thing. The word a person reads on screen is the word in
the code (models, functions, files, addresses) and in the docs.

- A new word goes here before it is used anywhere. Each part adds its words
  in step 1 of the loop (`CONTRIBUTING.md`), and fills its "In code" names
  then.
- The client's own words are used wherever they are clear; a cleaner word
  only where his is unclear.
- No software words on screen: never inventory, SKU, invoice, tenant or CRM.
- "Never say" holds the words we do not use, on screen or in code.

## The business

| Say | In code | Never say | Means |
|---|---|---|---|
| Business | `Business` | tenant, company (for the business) | The rental business that uses the system, with all its branches |
| Branch | `Branch` | | A separate unit of the business, with its own godowns and possibly its own partners. One today |
| Godown | `Godown` | warehouse, store | A storage place. One today |
| Section | | sector | One part of the business: Godown, Sales or Accounts. The work of one or more roles, not a record |
| Accounts | `bills` (its app) | | The section of final bills and payments, the Accountant's work. Its app is `bills`, so the word never meets the `users` app |

## Stock

| Say | In code | Never say | Means |
|---|---|---|---|
| Item | `Item` | product, SKU | One type of thing the business rents out |
| Category | `Category` | | A group of items: Counters, Serving Vessels, Cloths, Premium (showpieces and premium vessels) |
| Piece | | unit | One single thing of an item. Every count is in pieces |
| Stock | | inventory, quantity on hand | How many pieces of an item the business owns |
| Available | | free stock | Pieces of an item that are free on a date: not booked, not out, not missing |
| Availability | | | How many pieces of each item are available on each date. Always right: the client's first rule |
| Purchase price | `purchase_price` | cost price | What one piece cost the business. Also what the customer pays for a broken or missing piece |
| Rent | `rent` | rate, price (alone) | What the business charges for one piece per booking. The same for every event and every customer |

## Sales

| Say | In code | Never say | Means |
|---|---|---|---|
| Customer | `Customer` | client, party (alone) | Whoever books: an event company or a direct party |
| Event company | | | A customer that is another event management company. Most bookings |
| Direct party | | | A customer who books for their own event. Rare, but allowed |
| Estimate | `Estimate` | quotation, quote | The price offer, before the customer confirms |
| Follow-up | `FollowUp` | reminder | A reminder to call the customer back about an estimate |
| Booking | `Booking` | order (alone), event (for the booking) | A confirmed order. It holds its pieces for its date. An estimate becomes a booking |
| Event details | | | On a booking: event date, venue, setup date and time, site manager, service staff needed |

## Godown

| Say | In code | Never say | Means |
|---|---|---|---|
| Delivery and setup | | | Items leaving the godown, and the team arranging them at the venue |
| Loading Sheet | | printout, challan | The printed list for one booking: ticked while loading, carried to the site, checked on return |
| Out | | dispatched | A booking whose items have left the godown. The Godown Manager marks it in one step |
| Site manager | | | Leads the team at the venue. Works only from the Loading Sheet and does not sign in (Release 1) |
| Return check | | | The Godown Manager counting the items that came back |
| Missing | | lost | A piece that did not come back |
| Broken | | damaged | A piece that came back broken |
| Missing & Damage list | | | The missing and broken pieces of one booking, with their charges. The godown makes it; the office sends it with its bill |
| Recovered | | | A missing piece brought back, or collected by our staff. No longer charged, and available again |
| Charged | | | A missing or broken piece added to the final bill at its purchase price, and taken out of stock |
| Borrowed item | `BorrowedItem` | sub-rental | An item taken from another event group for one booking. Not stock |

## Accounts

| Say | In code | Never say | Means |
|---|---|---|---|
| Extra charges | | expenses | Transport, Loading & Unloading, Washing, and Setup and Service staff when billed apart. One typed total each, paid by the customer |
| Discount | `discount` | | An amount taken off the final bill. Decided only by the Accountant or the Owner, when the final bill is made |
| Round-off | `round_off` | roundup | Rounding the final amount, like 48,763 to 48,760 |
| Final bill | | invoice, event bill | Rent, plus extra charges, plus missing and damage, minus the discount, plus or minus the round-off |
| Payment | `Payment` | installment, advance (alone) | Any money received against a booking: an advance, the full amount, or one of several parts |
| Balance | | due, outstanding | What is still to be paid: the final bill minus all payments |

## People

| Say | In code | Never say | Means |
|---|---|---|---|
| User | `User` | account, login (for the person) | Someone who signs in: an Owner, Accountant, Office Staff or Godown Manager |
| Role | | group | A user's part in the business: Owner, Accountant, Office Staff or Godown Manager |
| Staff | | | People who work for the business: setup crew, service boys, godown workers. Most never sign in. Release 2. Django's own `is_staff` only lets a person into the Django admin; it never means staff |
| Service staff | | | Catering boys or service boys sent to an event |
| Sign in | | log in | Start using the system |
| Sign out | | log out | End the session on this device |
