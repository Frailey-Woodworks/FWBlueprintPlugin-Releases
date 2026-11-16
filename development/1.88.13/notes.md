Development comparison build; not a stable release.

Fix endless loop in DashedLineStyle.Ensure (Rhino 8 FindName never returns null)

Source build: fix21-final
Original build: 2026-11-15T00:34:51 America/Chicago
Source commit: 81df88e17d3a577118ff7e62abd1ffa7488e531d
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: 08126be41de9cd8741e7ed50770da158401952ed

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. Changed-IL negative control rejected.

Grouped round steps:
- afbb0ba Record FIX20 batten measurements, checks and native handoff
- 81df88e Fix endless loop in DashedLineStyle.Ensure (Rhino 8 FindName never returns null)

Signed package, both Rhino runtimes. Select this Dev version in Updates to pin it; automatic updates pause. It loads on the next normal Rhino start. Historical drawing behavior retained; no new native visual acceptance claimed.
