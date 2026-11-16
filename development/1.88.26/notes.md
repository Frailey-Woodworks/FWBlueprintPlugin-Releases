Development comparison build; not a stable release.

fix: recheck remaining dimension crossings after placement

Source build: fix34-44
Original build: 2026-11-16T05:13:16 America/Chicago
Source commit: 82c8fb5de9c17a77e6d67c2c8a1856e349a405cb
Picker commit: 1a7127b0d28d3d81b0ba11df9640cf09fcf9affb
Release source: f26c100ab43bd68f5142b45cc724c3c46b55922b

Match: exact rebuilt compiled IL and metadata after excluding version labels and MVID/build-header identifiers. Changed-IL negative control rejected.

Grouped round steps:
- c1e3811 Record FIX32 native failure audit, local verification and acceptance limits
- 375fe0c fix34: keep measured compositions, repair text lanes and concise CNC notes
- e020f2b fix34: refine oversized native frames and keep all shell panels stacked
- f213c0a fix34: measure full-size leader text and bound recovery to its own lane
- a60966b fix34: preserve CNC view anchors and above-view captions
- 34b8b67 fix34: retain exact producer guard around the new heading placement tag
- b95b0ff FIX34 revalidate native fit brackets and retain first-sheet companions
- ac59095 FIX34 qualify companion recovery against superseded split contract
- 8a6ff88 FIX34 pack feature callouts and anchor CNC edge labels
- dd36b85 Restore ordinary span readability and bound diagonal clearance
- 373d734 Measure leader glyph outlines and repack cleared caption space
- 6a6fb03 Keep measured CNC zero and axis labels apart
- 8fdc500 Recover colliding dimensions without displacing clear spans
- 488f26a Preserve caption reading order through native reflow
- ba6dc29 Apply native glyph scale and retain shelf CNC right-side relationship
- ad1a713 Keep legacy leg recipes outside ordinary-part sharing checks
- 3a0f259 Trace final native dimension fit and text positions for FIX34 review
- 5889948 Keep native text placement diagnostics compatible with managed adapters
- 146e052 Anchor CNC edge callouts to stock instead of wide instruction paragraphs
- 5c16f13 Wrap handle machining paragraphs to their measured instruction field
- ba63fcf Reset stale ordinary dimension text points and clear CNC axis labels
- 41817ef fix34: tighten above headings and bound handle instruction bands
- 3a7fba2 fix34: retain frame slats below opening view during recipe reflow
- 0f18ba2 fix34: put physical parts before CNC views in shared rows
- 367389e fix34: trace native dimension state through placement stages
- 38a5dab FIX34 qualify diagnostic environment access for native build
- f7b6d9c FIX34 anchor frame captions to their cut parts and trace rejected dimension lanes
- 73ef434 FIX34 keep long dimension text beside its span and clear its own line
- 0994014 FIX34 keep recovered chain lettering inside its measured panel
- 0fe4c36 FIX34 clear CNC axis lettering when both nearest sides are blocked
- 2d13c1b FIX34 reflow measured whole groups before splitting native pages
- 117d083 Fix short middle-chain labels without a false free end
- 27dec57 Retain measured right-side CNC notes in compact frame recipes
- 9a02a99 Apply compact CNC note placement to ordinary frame-door recipes
- 21c92bc Recover fitting page subsets and clear CNC X labels beside callouts
- 039c71d Prevent moved dimension lines from crossing clear neighboring text
- 17320a6 Compare tighter complete-view grids before shrinking companion recipes
- dcf04cf Keep short free-end dimensions near their parts across blocked lanes
- c68329d Place dimensions before repacking movable above-view headings
- 45ea2b8 Preserve chain identity during recovery and shorten internal slat captions
- 80a603f Snapshot chain measurements before native object replacement
- 4dac05c fix: include CNC companion in physical recipe grid cost
- fa332c8 fix: place dimensions before movable CNC captions
- 82c8fb5 fix: recheck remaining dimension crossings after placement

Signed package, both Rhino runtimes. Select this Dev version in Updates to pin it; automatic updates pause. It loads on the next normal Rhino start. Historical drawing behavior retained; no new native visual acceptance claimed.
