Development build; not a stable release.

Built on 1.88.18 (fix26, Friday's set), the last version you approved. None of the 1.88.19-1.88.28 dimension changes are included.

What changed:
- Handles: a handle whose model geometry is damaged (Naveen's right door pull has a slit seam) is now drawn from a repaired copy. Your model part is never changed.
- Record wells: the floor-clearance dimension is measured on the record-well drawing itself. Naveen no longer fails at "Record wells".
- One failure no longer stops the blueprint: a part, dimension or caption that fails stays drawn as far as it got, gets a red "INCORRECT: <part> - <reason>" note, and the rest of the sheets are still made. The command line lists every marked part.

Checked: Naveen runs natively and completes (7 cut sheets, 22 build pages). Signed package, both Rhino runtimes, 32 updater checks passed.

Source commit: 4be0e20611aebec2240e426416246d510b286dba
