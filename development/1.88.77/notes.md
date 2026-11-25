## Dev 1.88.77: Title Page works again (hotfix)

The Sales sheet's columns were rearranged, and Title Page stopped with "Sales contact headers changed. Nothing changed." It now finds each Sales column by its header name, wherever the column sits.
- Missing optional columns (Phone, Email, Destination, Special Notes, Estimated Weight, Hardware List) are left blank, with a note instead of stopping the command.
- A missing required column (#, Client, Project Type, Wood Type) names itself in the error.
- Only the needed columns are read, never the financial ones.

Tested against the live Sales sheet: client Amanda Ghassaei, piece 320, matched Admiral / Cherry.

Everything else is identical to 1.88.76. The larger batch of today's notes follows as 1.88.78.
