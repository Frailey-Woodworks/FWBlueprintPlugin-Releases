Development build for comparison; not a stable release.

Source build: fix37-13
Original build: 2026-11-16T08:55:11 America/Chicago
Source commit: 7705750a7166c8ad70a18ff04c8511d834de5fd7
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: 836458b46795f381f8ed6e85b3c8000b894255cd

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. Negative control changing an IL instruction was rejected.

Grouped round steps:
- feb8883 Record FIX35 stopped build-only candidate and unresolved native acceptance
- 262faa6 FIX36 diagnose sleep-interrupted timeout and bound native execution window
- f06df52 FIX37 restore fixed model-size lettering and remove paper text composition feedback
- d6055d2 FIX37 keep complete base on the last page and restore nearby captions
- 1a331eb FIX37 preserve the entire plain base as one measured page companion
- ac0fc47 FIX37 arrange base before grouping and preserve Friday membership when page count ties
- 7291191 FIX37 compose door battens as an attached block for balanced Tabitha pages
- 380780a FIX37 use actual native group labels and record style and view separation evidence
- e126f18 FIX37 retain base page membership through the final balance pass
- 57a0b0b FIX37 match Friday wall and shelf-door columns using native measured groups
- 1d4f704 FIX37 align physical panel tops in the Friday two-column arrangement
- 56e836b fix: isolate door and drawer sheets and remove frame opening links
- f3aa17c fix: preserve caption word spacing with model-scale lettering
- 4e88258 test: gate focused model-scale iterations and preserve native conformance
- 7705750 fix: restrict batten page companions to doors

Signed package, both Rhino runtimes. Choose this Dev version in the Updates tab to pin it. It loads on the next normal Rhino start; no Rhino window is closed. Historical drawing behavior is retained; this is not new native visual acceptance.
