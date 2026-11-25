## Dev 1.88.70 — ChamferAngle fix for Rhino boxes

- ChamferAngle now works on objects stored as extrusions (Rhino's Box command makes these by default). Before, picked edges on an extrusion box could not be mapped and nothing was chamfered.
- Hidden-Rhino qualification: FWChamferAngleSelfTest passes every case (22.5/45/60 degree boxes, flips, Short/Long length, convex wedges, extrusion boxes, curved and concave edges skipped).
- Build-package group keeping (1.88.69) verified in hidden Rhino on the Jennifer copy: 12 console groups kept on their pages, all other parts loose.
