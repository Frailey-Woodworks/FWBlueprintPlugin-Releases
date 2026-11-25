Title Page fix.

- The Title Page command stopped with "The Contact Info: value does not fit" and made no page. Cause: a newer text-size rule for build pages (labels at model scale 12) was also being applied to the title page. That shrank each value's wrap width to about 0.11 inch, so the text stacked one word per line and overflowed its cell.
- The title page now uses its own sizes again: values 0.08 in, Client Name 0.11 in, Project Type 0.12 in, each wrapped to its 1.375 in cell.
- Tested in hidden Rhino on a copy with fake client data. The previous build reproduced the same error, and this build placed every value inside its cell.
