Development comparison build; not a stable release.

Persist caught Console rollback and visibility errors

Source build: fix13-final
Original build: 2026-11-14T12:47:27 America/Chicago
Source commit: 9b616342c99811f21aa3f0cfe22ad565d22e0af9
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: 63c226b52455384ba436c859a0a32bee19cdf0ca

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. Changed-IL negative control rejected.

Grouped round steps:
- 64ad77c Record Fix 12 verification and native review handoff
- 033b139 Record every Console failure with its original stack
- 189828e Fix capped-wall dimension placement in sheet coordinates
- 9b61634 Persist caught Console rollback and visibility errors

Signed package, both Rhino runtimes. Select this Dev version in Updates to pin it; automatic updates pause. It loads on the next normal Rhino start. Historical drawing behavior retained; no new native visual acceptance claimed.
