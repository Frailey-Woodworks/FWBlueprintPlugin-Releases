# Rhino Blueprint Plugin downloads

Created October 20, 2026. Updated October 20, 2026.

Compiled Windows Rhino 8 packages only. No GitHub account is needed to download them. Application source stays in the private Frailey Woodworks repository.

Download the ZIP from the latest release, extract it to a permanent folder, and drag `net7.0/FWBlueprintPlugin.rhp` into Rhino 8. Run `BlueprintUpdates` for version information, automatic-update controls and rollback. Future verified updates load at your next normal Rhino start.

Packages and release metadata are signed. This repository contains distribution infrastructure and compiled artifacts, never application source, debugging symbols, customer models, Google credentials or owner access tokens.

Final version 1.80.2 passed anonymous signed-download and failure checks. In actual Work Rhino, Check now staged the newer release while the old version kept running; a normal blank-session restart loaded 1.80.2 before any Blueprint command. All update controls were visually checked. Automatic startup checking was separately observed; its normal cooldown was preserved. Native rollback and client-model workflow regression were outside this update check. See each release's notes for current limits.

[Download version 1.80.2](https://github.com/Frailey-Woodworks/FWBlueprintPlugin-Releases/releases/download/v1.80.2/FWBlueprintPlugin-1.80.2-win-x64.zip)
