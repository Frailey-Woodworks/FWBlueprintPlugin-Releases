Development comparison build; not a stable release.

FIX30 withhold incomplete CNC setups when source loops are invalid

Source build: fix30-final
Original build: 2026-11-15T22:02:22 America/Chicago
Source commit: 6c5fcb9420e231c7070baf3c61cb629702f5f846
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: d32cd9c50dbafbb942dde23978a48fc3407e4c7e

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. Changed-IL negative control rejected.

Grouped round steps:
- 98538a6 Record FIX29b evidence, throw audit and native acceptance limits
- 9cf4b20 FIX30 add source-derived panel CNC layouts and enforce cut-page rules
- 2d97ada FIX30 keep secondary labels out of shell roles and show CNC limits
- 6c5fcb9 FIX30 withhold incomplete CNC setups when source loops are invalid

Signed package, both Rhino runtimes. Select this Dev version in Updates to pin it; automatic updates pause. It loads on the next normal Rhino start. Historical drawing behavior retained; no new native visual acceptance claimed.
