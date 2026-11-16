FW Version Manager is a small, separate Rhino 8 plug-in that switches the Frailey Woodworks Toolkit to any published version, including old versions that have no version picker of their own. This is not a Toolkit release.

Install
1. Download `fw-version-manager-1.0.0-win-x64.zip` below and extract it to a folder you will keep.
2. Drag `net7.0\FWVersionManager.rhp` into the Rhino 8 window.
3. Type `FWVersionManager`.

Pick a version and press "Install selected version". It is downloaded with no sign-in, checked against the publisher's signature and checksums, and loads the next time you start Rhino. Rhino is never closed for you. The choice stays pinned until you pick another version or press "Return to latest stable".

Signed package, both Rhino runtimes, one self-contained assembly. Background checks passed (listing, signature/tamper refusal, registration switching on a scratch key, real public Toolkit packages 1.80.0 to 1.88.28). Not yet loaded in Rhino: the owner's first install is the native check.
