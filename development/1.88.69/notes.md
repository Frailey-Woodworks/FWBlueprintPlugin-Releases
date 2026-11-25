## Dev 1.88.69 — Build package keeps your console groups

Amendment to the "build package parts are never grouped" rule (Dev tab switch `R-BUILD-KEEP-GROUPS`):

- A part that was grouped on the original console (for example a frame-and-panel door) stays grouped on each build-package page, so it moves and deletes as one item.
- One group per console group per page, made only when two or more of its parts are on that page.
- Every other part stays ungrouped; the console model itself is never changed.
- OFF: every build-package part is ungrouped, as in 1.88.68.

Note: published at the owner's request before the hidden-Rhino build-package check ran; build and Dev-tab tests pass.
