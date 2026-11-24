# Rules: roles

The rules of Users and roles (`docs/MODULES.md`): who may do what. Built in
step 1 (`docs/PLAN.md`), with the roles ADR, which is built from this file.
Which screens each role opens: `docs/SCREENS.md`. Words:
`docs/GLOSSARY.md`.

- Each rule has an ID. A test names the ID of the rule it protects.
- An ID never changes. A new rule takes the next free number.
- Step 1 checks these rules again before it builds them, and each part's
  loop checks its own rows in "Who may do what".

## The roles

- **ROLE-1** Four roles sign in: Owner, Accountant, Office Staff and
  Godown Manager. They are fixed in the code: a business never makes its
  own roles, and never changes what a role may do. A change comes in a
  release.
- **ROLE-2** A role belongs to a person's place in the business, their
  membership, never to the user. So a second business or branch can later
  give the same person another role.
- **ROLE-3** Users are not staff. The site manager does not sign in in
  Release 1, and works from the printed Loading Sheet.
- **ROLE-4** The Owner may do everything. In the code, each permission
  still names the Owner, one by one, like every other role (ROLE-5).
- **ROLE-5** A new role starts with no permission at all, and is given
  each one by name.

## How a page is guarded

- **ROLE-6** A page, a menu item, a form or a template asks for a
  permission, like "change a rent", never for a role. A test fails when
  any of them checks a role by its name.
- **ROLE-7** Who has which permission is written once, in the code. A
  permission moves to another role with one line, and no page changes.
- **ROLE-8** A menu item, a button or a link shows only to the roles its
  page lets in. A door a role can see but not open is worse than no door.
- **ROLE-9** A box a role may not change is left out of its form, so the
  server never takes that value from that role, even if it is sent.
- **ROLE-10** A signed-in person whose role may not open a page gets "Not
  open to your role", with none of the page's data (`docs/DESIGN.md`,
  Screen states).
- **ROLE-11** Every page is tested for every role, with the answers typed
  by hand, never read from the list of permissions.

## Who may do what

The Owner may do all of it (ROLE-4). Each row is the default, to confirm
with the client (`docs/MODULES.md`, point 16). An empty cell means no.

### Stock (step 3)

| ID | Action | Accountant | Office Staff | Godown Manager |
|---|---|---|---|---|
| ROLE-12 | See the purchase price (point 2) | Yes | | |
| ROLE-13 | Add an item, with its first rent | | Yes | Yes |
| ROLE-14 | Change an item's name, category or photo | | Yes | Yes |
| ROLE-15 | Change a saved rent. Saved estimates and bookings keep the rent they were made with | Yes | | |
| ROLE-16 | Set or change the purchase price | Yes | | |
| ROLE-17 | Change the count, with why | | | Yes |

- Only the two who give discounts change a saved rent (ROLE-15), so
  nobody else can give a hidden discount by lowering a rent before an
  estimate.
- If Office Staff need to change saved rents while they type the first
  stock list, they are given ROLE-15 for those weeks only, and the client
  is asked.

### Estimates and bookings (step 4)

| ID | Action | Accountant | Office Staff | Godown Manager |
|---|---|---|---|---|
| ROLE-18 | See the money of an estimate or a booking: its rent, charges, payments and balance | Yes | Yes | |
| ROLE-19 | Add or change a customer | | Yes | |
| ROLE-20 | Make or change an estimate, and set its follow-ups | | Yes | |
| ROLE-21 | Make an estimate a booking | | Yes | |
| ROLE-22 | Change a booking | | Yes | |
| ROLE-23 | Cancel an estimate or a booking, with a reason | | Yes | |
| ROLE-24 | Add a borrowed item line (step 7) | | Yes | |
| ROLE-25 | Print or share an estimate | | Yes | |

### Godown (step 5)

| ID | Action | Accountant | Office Staff | Godown Manager |
|---|---|---|---|---|
| ROLE-26 | Print the Loading Sheet and the delivery list (point 22) | | | Yes |
| ROLE-27 | Mark Out, correcting any line that loaded short | | | Yes |
| ROLE-28 | Do the return check, and save the count | | | Yes |
| ROLE-29 | Mark a missing piece Recovered, once it is back in the godown | | | Yes |
| ROLE-30 | Mark a borrowed item given back to its owner (step 7) | | | Yes |
| ROLE-31 | Print or share the Missing & Damage bill | Yes | Yes | |

### Accounts (step 6)

| ID | Action | Accountant | Office Staff | Godown Manager |
|---|---|---|---|---|
| ROLE-32 | Add the extra charges | Yes | | |
| ROLE-33 | Give a discount, and choose the round-off | Yes | | |
| ROLE-34 | Make the final bill | Yes | | |
| ROLE-35 | Print or share the final bill | Yes | | |
| ROLE-36 | Record a payment (point 18) | Yes | | |
| ROLE-37 | Correct a payment, kept with who, when and what it was | Yes | | |

### Owner only

| ID | Action | Step |
|---|---|---|
| ROLE-38 | Add a user with a role, turn one off, or set a new password | 1 |
| ROLE-39 | See the owner dashboard, if it is built (point 7) | 8 |
