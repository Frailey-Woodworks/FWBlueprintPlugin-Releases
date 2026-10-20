# Binary distribution repository

This repository is PUBLIC. Only compiled plugin packages, signed release metadata, public signing keys, installer instructions and release-publishing infrastructure belong here. Never add application C# source, PDBs, private keys, credentials, client files, models or screenshots.

Before edits inspect the working tree, branch and remote; pull the upstream with `git pull --ff-only`. Preserve all existing work. After task-specific changes, verify the package/signature checks, commit only task files and push. Verify the push succeeded. Never force push, discard changes or commit secrets. For initial creation there is no upstream until the first push.

Private source is Frailey-Woodworks/FWBlueprintPlugin. Release version directories are immutable. Never replace a published version or repoint its tag. Correct releases require a new source version. One writer owns each publication. Do not change the private repository's visibility.

Release artifact bytes are binary-preserved with .gitattributes, including signed JSON metadata. Verify signatures after a fresh checkout, not only before git add. October 20 initial unpublished upload failed because Git changed JSON CRLF to LF; original signed bytes were restored before any release was published. No published package was replaced.
