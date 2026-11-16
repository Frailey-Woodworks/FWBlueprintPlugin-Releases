Development comparison build; not a stable release.

Fix native layout recovery, paper-fit feedback and drawing identity handling

Source build: fix32-final
Original build: 2026-11-16T00:22:16 America/Chicago
Source commit: b8e4e687abc9a2241000cd6fe0dade224f97a257
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: 9fba7b4acdc5dc4bdbecabf80aa48a7ee9e3794d

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. Changed-IL negative control rejected.

Grouped round steps:
- 4d482d9 Record FIX31 verification, owner calibration and native review limits
- b8e4e68 Fix native layout recovery, paper-fit feedback and drawing identity handling

Signed package, both Rhino runtimes. Select this Dev version in Updates to pin it; automatic updates pause. It loads on the next normal Rhino start. Historical drawing behavior retained; no new native visual acceptance claimed.
