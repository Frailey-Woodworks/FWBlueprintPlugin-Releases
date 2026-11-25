## Dev 1.88.76: all of the owner's 2026-11-25 notes in one release

Every change has its own Dev-tab switch. The Dev tab shows only this version's switches.

**Build package**
- Notes are plain red text next to their feature, with no leaders. Lines wrap by text-block width, with no hard line breaks.
- All text and dimensions use the default style at model space scale 12; the per-page text scaling is gone. Titles are unchanged.
- Dimensions sit 4" off the measured surface, or 8" on sub-assembly isos.
- The part in front is ghosted with FW Ghosted on sub-assembly pages.
- Sub-assembly isos get an overall joined dimension where they already have plan dimensions.
- The leg-post alignment lines are gone.
- When the sides come to the case, the near side is shown attached and the far side 6" out.
- The edge-details page is rebuilt to match the owner's goal:
  - a scaled, ghosted console with only the machined faces red;
  - edge-face strip elevations with a break mark and red chamfer bands;
  - a right-hand column, and the summary as a list.

**Cut sheets**
- A panel's label sits 2.5" below the panel; there is 5" to the next block below and 5" between side-by-side blocks. CNC views line up with the top of the panels.
- Perm shelf CNC orientation uses the cut bounding-box centre nearest XY 0. Every CNC instruction says "(top face up)" or "(underside face up)".
- Raised-panel interior walls go in as a mirrored pair: inside face up, front edges together, one continuous cut outline with a 1/4" overcut at the stock edges and a 1/2" exit pad.
- The CNC note goes right of or below the CNC view, whichever gives the smaller page.
- Door groups: overall width on top, the width chain on the clear side, overall height and the height chain on opposite sides. On a flanked column the chain goes inset, 3" in from the right edge.
- Record well: the assembled view gets the front-to-back clear dimension, plus the raised-floor rise when there is one.
- Loose surfaces that close into a solid are joined in the working copy, never in the owner's file. Parts are measured in their own orientation.

**Tools**
- Dim3D: type a number at "Dimension line location" to lock the offset distance.

Tested in hidden Rhino on FW-NEWPC through round 16 on Jennifer, Kathryn, Tabitha and Shelley. The round-17 check run is still in progress at publish time.
