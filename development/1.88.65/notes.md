# 1.88.65 (development)

Title: Priority-ranked cut sheet grouping

- Cut sheets: panel drawings are grouped by ranked rules instead of fixed buckets.
  1. No island sheets: a plain cut group never sits alone when a readable companion exists. Complete recipes (door CNC, legs, wine rack, record well, drawer boxes, CNC layouts) keep their own pages.
  2. Families stay together: exterior walls with their leg caps; all shelves, removable and permanent.
  3. Sheet 1 is top + bottom; the back joins only when all three print at a normal size.
  4. At most one extra sheet per console; within that, the plan with the biggest text wins.
- On the 12 test consoles: no islands remain, split families drop on 9, the smallest casework text gets bigger on every console, and 9 consoles gain one cut sheet. Part sizes and quantities are unchanged.
- Dev switch R-SHEET-PRIORITY: OFF restores the 1.88.64 grouping.
