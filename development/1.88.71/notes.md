## Dev 1.88.71 — Build package matches the Jennifer goal blueprint

Ten changes, each with its own Dev tab switch (OFF restores 1.88.70):

- **R-BUILD-ALL-BLACK** — no grey earlier parts on any build page.
- **R-BUILD-SUBASSEMBLY-TITLES** — no titles on main steps; sub-assembly pages keep a plain title.
- **R-BUILD-NO-DOOR-PREP** — door-preparation pages left out for now.
- **R-BUILD-SUBASSEMBLY-NEXT** — sub-assembly pages sit right before the step that installs them; redundant side-fit pages dropped for mirrored sides.
- **R-BUILD-JOINED-ONLY** — a step shows only the parts that actually touch there; "flush on back edge" note and shelf size dims.
- **R-BUILD-DIM-NEAR-PART** — front-view dims sit beside the part they measure.
- **R-EDGE-ON-BUILD** — no edge-profile sheet in the cut list; profile leaders on the step that adds each part, and an "Edge details" page for parts with several profiles.
- **R-BUILD-CENTRED-NOTES** — centred walls/top get a centring note with measured overhang dims.
- **R-BUILD-SETBACK-BOTTOM** — door set-back note measured from the bottom edge.
- **R-BUILD-PAGE-MARGINS** — at least 1/6 of the page as margin on every side.

Note: published at the owner's request before the hidden-Rhino run on Jennifer; unit tests pass (82 goal-rule, 1,229 margin, Dev tab checks). If a page looks wrong, turn that switch off in the Dev tab.
