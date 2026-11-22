# 1.88.52 (development)

Away-run refinements Claude chose for itself (R-OWN-ROADMAP). Each is separable and awaits owner Keep/Reject.

- Build package: the side-location steps always show the left side first, then the right. Scott, Jeff, Standard-Crosby and Shelley-Kathryn used to show the right side first.
- Glue check: metal parts (Robin and Cortney's brass foot caps) are hardware and are never counted as glued.
- Door CNC notes: when two door families on one console share an insert type, the file names are numbered ("louvered mesh doors 1" / "2"), so one program can't overwrite the other. Found on Cortney.
- Door sheets: on short openings the opening-width line moves up so its label no longer prints on top of the height label (Cortney door family 2).
- Title stock order: the back panel is named as sheet goods with its size ("not in bf"), so the sheet is still ordered. Unit-tested; the harness doesn't run the title command.
- Tests: SidePlannerTests compiles and passes again. It had been broken since 1.88.38. Its expectations were updated for mirrored sides and the removable lift-lid front plate.

Verified: all 12 consoles native (rr4), 0 L glue-ups, no failures. Final commit sampled natively (rr7: Kathryn, Cortney, Jeff); the only differences from rr4 are hidden-line dash phase.
