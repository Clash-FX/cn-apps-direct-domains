# Contributing

Thanks for helping keep this domain list accurate and safe.

## Adding a new app / service

1. **Confirm the domain is mainland-only.** This is the single most
   important check. A domain qualifies for this list only if:
   - It serves Chinese users from infrastructure inside or fronting
     mainland China.
   - It does **not** have a legitimate overseas-user routing path. (If
     an overseas user genuinely needs to reach this domain via proxy,
     it does **not** belong here.)

2. **Use the most specific suffix that still covers what the app needs.**
   - Prefer `DOMAIN-SUFFIX,music.163.com,DIRECT` over
     `DOMAIN-SUFFIX,163.com,DIRECT` if the user only needs music to work.
   - Add `163.com` only when the app legitimately needs the entire suffix.

3. **Verify the app actually queries those domains.** Easiest method:
   - Open ClashFX → Connections viewer
   - Trigger the app's main feature (e.g. play a song, log in, push a
     notification)
   - Note every distinct domain the app touches
   - Cross-check against the app's privacy policy / DNS records if
     available

4. **Edit `apps-direct-domains.list`.** Add the rules in the matching
   category section.

5. **Open a PR.** Title: `Add <App Name>`. Body should include:
   - The app/service you're adding.
   - The list of domains you observed it using.
   - Confirmation that the domains are mainland-only.

## Removing or scoping down an entry

If an entry is too broad and inadvertently captures overseas traffic
(e.g. you discover `qq.com` also fronts an overseas service the user
wanted via proxy), open an issue first to discuss. Possible fixes:

- Drop the broad `qq.com` rule, replace with more specific subdomains.
- Add a `# overseas exception` note.

## Renaming domains

If a Chinese service changes its primary domain across versions, include
**both** the old and new domains so users on older app versions still
match.

## What NOT to add

To keep this list trustworthy:

- ❌ Generic CDNs that serve both Chinese and overseas tenants (e.g.
  bare `cloudflare.com`, `akamai.com`, `fastly.net`).
- ❌ Apple / Microsoft / Google domains (handle these in your main rules).
- ❌ IP ranges (`IP-CIDR`). Use `GEOIP,CN,DIRECT` separately.
- ❌ Domains for the international versions of Chinese apps (e.g.
  `larksuite.com`, `tiktok.com`).

## Format

Plain mihomo / Clash classical rule-provider syntax. One rule per line.
Comments start with `#`. Keep the section dividers
(`# === Category ===`) for readability.
