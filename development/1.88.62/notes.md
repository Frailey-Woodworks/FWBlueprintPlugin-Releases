# 1.88.62 (development)

Title: Ghost and Unghost respect groups

- Unghost: picking one ghosted object in a group now unghosts the whole group, the same as a normal Rhino click selects a group. Before, Unghost picked single objects and bypassed groups. In a group where only some members are ghosted, the ghosted members are unghosted and the rest are left alone.
- Ghost: picking inside the command also selects the whole group (pre-selected objects were already group-aware through Rhino's normal click).
