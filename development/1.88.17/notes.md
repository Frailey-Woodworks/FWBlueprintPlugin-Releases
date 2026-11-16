Development comparison build; not a stable release.

Restore legacy drawer compaction before adaptive recipe placement

Source build: fix25-final
Original build: 2026-11-15T03:39:10 America/Chicago
Source commit: 0747586af489150e0d2d9d80f5e4d96dcb052c4d
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: 67cfe4d64cf0926f1a64de6b35ddf1bdf30d4930

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. Changed-IL negative control rejected.

Grouped round steps:
- 62138fc Record FIX24 calibration, complete-packet checks and native handoff
- 0747586 Restore legacy drawer compaction before adaptive recipe placement

Signed package, both Rhino runtimes. Select this Dev version in Updates to pin it; automatic updates pause. It loads on the next normal Rhino start. Historical drawing behavior retained; no new native visual acceptance claimed.
