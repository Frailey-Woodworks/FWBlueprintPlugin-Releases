Development build for comparison: FIX26, Friday's set. Not a stable release.

Source build: fix26-final
Original build: 2026-11-15T04:12:53 America/Chicago
Source commit: 47ce46c0ad38d7df4f9836dc08be19d7d564d267
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: dfe3bc0be969b1d4c2056f5b85e02948ebdc2684

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. A changed-IL negative control was rejected.

Grouped round steps:
- 324d1ef Record FIX25 compact recipe verification and native handoff
- 47ce46c Keep complete drawer recipes when compaction or readability preferences fail

Signed package, both Rhino runtimes. Select this Dev version in Updates to pin it; automatic updates pause. It loads on the next normal Rhino start. Historical drawing behavior retained, not new native visual acceptance.
