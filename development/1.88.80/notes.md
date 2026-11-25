Batch of your notes since 1.88.76. Each change has its own switch on the Dev tab.

Build package and pages
- Notes are plain 2-line text with no leaders. Dimensions sit 4" off their surfaces; small labels use the default size at model scale 12 (8 for CNC and view labels).
- Front assemblies are no longer pre-ghosted, and sub-assembly pages carry no dimensions. No dashed leg alignment lines. On two-side installs the near assembly stays attached and the far one moves 6" out.
- Cut list and build package are placed 20 ft up in the top view, clear of the console. A new Build Package version layer is added only when the Blueprint parent already holds one.
- Cut-sheet titles align to the final panel and dimension line, and gaps are 2.5" / 5".
- The Dim3D command accepts a typed offset.
- FW Ghosted has isocurves off.

Edge details pages
- Measured edge rules. A true router-bit angle reads "<angle>° chamfer", with its clean leg dimensioned. A track-saw cut reads "<depth> deep angle cut". Roundovers get R- radius dimensions.
- A zoomed corner circle shows the machined faces in red and the flat faces in grey.
- Two section views (front, side), captions 3" higher, and one wrapped summary block.

CNC and doors
- Perm shelf orientation uses the bounding-box centre, with the face-up note. Raised-panel interior walls follow your outline, pad and label rules. Mesh doors keep their offsets.
- CNC labels are anchored, with even spacing. Door-group and record-well dimensions follow your examples.

Cut sheets
- In a row of panels with different heights, the common height goes on the left. Each different panel gets its own height dimension 3" in from its right edge (Admiral Rem Shelves).

Cutlist command
- Every part is laid out longest left to right, second top to bottom, thinnest vertical, with overall length and width only. Curved and splayed parts are turned to their tightest box.
- One problem part can no longer stop the whole cut list; it is skipped and named with the reason.
- Parts whose model geometry is damaged (like two curved Everyday Desk pieces) are drawn from their surfaces.

Title Page
- The size and console-picture fixes from 1.88.78 and 1.88.79 are included.

Tested in hidden Rhino on Jennifer, Kathryn, Tabitha, Shelley and the Admiral, on the Everyday Desk (all 42 v4 parts drawn with correct dimensions) and on the Title Page, with measured checks on every change.
