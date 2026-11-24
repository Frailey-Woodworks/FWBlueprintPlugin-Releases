# 1.88.63 (development)

Title: Door joint types and the Dev tab

- Door sheets: each frame door's joint type is read from the model. The original type is now named "half-lap joint". The new "stile and rail bit" type has rails between full-height stiles, with tongues measured from the model (3/8" fallback). Its rails are cut to the gap between the stiles plus both tongues, with no 1/4" allowance, and the cut view shows tongue lines instead of laps.
- Door sheets: the title gets a second line naming the joint, with a small corner-joint drawing in a circle beside it.
- Door sheets: solid-panel half-lap door views dimension the rail width (e.g. 2-1/2") at the right of the top rail.
- Door CNC drawings (solid panel): two more outlines around the window, one 1" outside it and one 1/8" inside it.
- New Dev tab (dev builds only): one switch per feature added since stable 1.88.41, with "All on" and "All off (= stable)". Hover a switch for a description and a before/after picture. Changes apply to the next command, with no restart. Run logs name any switches that were off.
- Stile-and-rail doors whose two rails differ in length get a warning instead of stopping the run.
