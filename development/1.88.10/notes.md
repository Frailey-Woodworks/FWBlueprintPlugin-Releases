Development comparison build; not a stable release.

Restore manual Console picks while preserving ConsoleAuto workflow

Source build: fix18-final
Original build: 2026-11-14T17:37:51 America/Chicago
Source commit: ee55490d7a27a990208d83633b76576eb83add1b
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: ecb80f2af5986a76ffd28c248d5894d7941fc5f6

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. Changed-IL negative control rejected.

Grouped round steps:
- c353eec Record FIX17 build checks, dash measurements and affected pages
- ee55490 Restore manual Console picks while preserving ConsoleAuto workflow

Signed package, both Rhino runtimes. Select this Dev version in Updates to pin it; automatic updates pause. It loads on the next normal Rhino start. Historical drawing behavior retained; no new native visual acceptance claimed.
