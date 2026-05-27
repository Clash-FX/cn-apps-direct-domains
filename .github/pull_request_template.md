## What this PR does

<!-- Add <App Name> / Drop <broad rule> / Tighten <existing rule> -->

## Inclusion check (for additions)

- [ ] Domain is mainland-only (no overseas tenant routing through it)
- [ ] Listed under the matching `# === Category ===` section
- [ ] No duplicate entry (the `Lint` workflow will catch this; this checkbox is the human pass)
- [ ] No `IP-CIDR` rules (combine with `GEOIP,CN,DIRECT` in your main rules instead)
- [ ] One app / change per PR (easier to review and revert)

## How verified

<!--
- Opened the app under ClashFX, used Connections viewer to list every domain it touched.
- Cross-checked WHOIS / ICP filings to confirm mainland-only.
- Tested that adding the rule actually makes the app's traffic go DIRECT.
-->

## Tested on

- macOS version:
- App version:
