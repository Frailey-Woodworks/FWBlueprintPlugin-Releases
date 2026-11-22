# 1.88.53 (development)

- Door sheets: when two door families share an insert type, the sheet header carries the family number, matching its CNC file ("Louvered + mesh frame doors 2"). Cortney; every other console is unchanged.
- Build package: a shelf clearance that repeats a span already measured within one label width is skipped. On Adam Wine's removable-shelves page, two "13 7/8" labels printed on top of each other. Found by the new in-Rhino label-overlap audit, which now shows 0 overlaps on every cut sheet and build page of all 12 consoles.
- Tests: the unit-suite runner decides failures by exit code, so dotnet warnings no longer abort it.
