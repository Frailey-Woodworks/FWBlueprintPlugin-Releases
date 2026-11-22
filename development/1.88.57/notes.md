# 1.88.57 (development)

- Build package: the wine rack is no longer one all-at-once glue-up. Each wall takes the members in its dados (one face direction) and the rails on its top and bottom edges (another), so the rack now builds as "walls and members" first, then "rails (second glue-up)" (Adam Wine).
- Glue check: the one-direction rule now also runs inside wine rack and drawer-box steps (compared by role; floating drawer bottoms excluded), so an L inside a sub-assembly is caught automatically. Unit test with an all-at-once rack as the positive control.
