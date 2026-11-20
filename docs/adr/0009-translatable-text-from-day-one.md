# 0009: Translatable text from day one; Malayalam later

**Status:** Accepted (2026-11-20)

## Context

- The client and his team work in Kerala. Malayalam screens may be wanted,
  for the godown above all; nobody has asked yet.
- Marking text while writing it costs little. Marking it later means finding
  every text in every file.
- Django has translation built in, so no new library is needed. It already
  ships Malayalam for its own screens, such as the admin.

## Decision

- **English is the source language.** Every text a person sees is written in
  English and marked for translation, from the first app:
  - templates: `{% translate %}`, and `{% blocktranslate %}` for text with
    values inside;
  - Python: `gettext_lazy` (imported as `_`) for labels of models, fields and
    forms and for error messages; `gettext` for messages made during a
    request;
  - JavaScript gets its text from the page (for example a `data-` attribute),
    so the template marks it.
- **Text with values inside uses named placeholders** (`%(name)s`), so a
  translation can put the words in a different order.
- **Not translated:** what people type (item and customer names, notes),
  numbers and codes, log messages, text only developers see (like the
  start-up error in `config/env.py`), and machine answers (`/health/`).
- **Set up now:** `LANGUAGES` lists only English, and `LOCALE_PATHS` points
  to `locale/`.
- **Malayalam comes when the client wants it:** fill `locale/ml/`, add
  `LocaleMiddleware`, and let each person choose a language.

## Consequences

- Each text takes a few more characters to write. It is a code rule in
  `CONTRIBUTING.md`, checked in review; there is no automatic check yet.
- When Malayalam starts, the work is translating a list of texts, not
  editing every screen.
- `makemessages` and `compilemessages` need the GNU gettext tools, installed
  when the first translation starts.
- Malayalam letters need a font that has them, on screens and on the printed
  Loading Sheet and bills. Checked when Malayalam starts.
