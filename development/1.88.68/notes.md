## Dev 1.88.68 — ChamferAngle command

New command **ChamferAngle** (Dev tab switch `R-CHAMFER-ANGLE`, on by default in dev builds):

- Select edges like ChamferEdges (preselection and ChainEdges work), type an angle (e.g. 22.5) and a length (e.g. 1/4).
- Live preview of each chamfer outline with both leg lengths labelled.
- **Ctrl** switches whether the typed length is the short leg (default) or the long leg.
- **Shift** flips which face gets the long leg for all edges; **FlipOne** flips one clicked edge.
- **Enter** applies everything as one undo, keeping layer, name and other attributes. **Esc** changes nothing.
- Works on straight edges between flat faces at any outside angle; curved edges, inside corners and chamfers wider than the face are skipped with a reason.
- Scriptable: `-ChamferAngle Angle=22.5 Length=1/4 LengthIs=Short Flip Enter`.

Note: published at the owner's request before the native hidden-Rhino self-test (FWChamferAngleSelfTest) ran; unit tests pass (1,017 geometry checks).
