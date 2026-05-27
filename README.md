# cn-apps-direct-domains

[English](README.md) | [简体中文](README_zh-CN.md)

Curated `DOMAIN-SUFFIX` bypass rules for common Chinese apps and services,
in mihomo / Clash classical rule-provider format.

This is the **domain-based companion** to
[`Clash-FX/cn-apps-direct`](https://github.com/Clash-FX/cn-apps-direct).

| Property                | `cn-apps-direct`                  | `cn-apps-direct-domains` *(this repo)* |
|-------------------------|-----------------------------------|----------------------------------------|
| Rule type               | `PROCESS-NAME,...`                | `DOMAIN-SUFFIX,...`                    |
| Works under Rule mode   | ❌ (no process info)              | ✅                                     |
| Works under Enhanced (TUN) | ✅                             | ✅                                     |
| Match precision         | App-exact (won't leak)            | App + shared infra (broader scope)     |
| Best for                | Enhanced mode users               | Rule-mode users / fallback             |

## Why two repos?

`PROCESS-NAME` is precise but requires TUN/Enhanced Mode — mihomo needs to
own the socket to inspect the calling process. Under classic system-proxy
(Rule mode), mihomo only sees domains and IPs, so `PROCESS-NAME` rules
silently fail there.

This list mirrors the same intent ("let common Chinese apps go direct")
using `DOMAIN-SUFFIX`, so it works regardless of the user's proxy mode.

## Usage

### Through ClashFX

A toggle that injects this list into the generated config is on the
roadmap and tracked in [Clash-FX/ClashFX#104](https://github.com/Clash-FX/ClashFX/issues/104).
Until then, use the standalone `rule-provider` setup below.

### Standalone (any mihomo / Clash client)

Add this to your `config.yaml`:

```yaml
rule-providers:
  clashfx-cn-apps-direct-domains:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/Clash-FX/cn-apps-direct-domains/main/apps-direct-domains.list
    path: ./ruleset/clashfx-cn-apps-direct-domains.list
    interval: 86400

rules:
  - RULE-SET,clashfx-cn-apps-direct-domains,DIRECT
  # ... your existing rules below
```

## Inclusion policy

To stay safe and predictable, this list **only includes domains that are
exclusively used by mainland-China-facing services.** That means:

- ✅ `weixin.qq.com`, `music.163.com`, `bilibili.com` — domestic-only.
- ❌ `larksuite.com` (Lark's international tenant), `tiktok.com` (TikTok
  international) — these legitimately need overseas routing for some users.
- ❌ `apple.com`, `microsoft.com` — global services; users should decide
  per case via their main rules file.

For an app with both domestic and international footprints (e.g. Feishu /
Lark), only the **`.cn`** / mainland-specific domains are added.

## What about IP rules?

We intentionally avoid `IP-CIDR` rules in this list. Domain-based rules
are easier to audit, less likely to break when CDN topology changes, and
play well with fake-IP DNS modes that some users run.

If you need IP-level Chinese routing, combine this list with `GEOIP,CN,DIRECT`
in your main rules. mihomo handles the precedence correctly.

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). In short:

1. Verify the domain is **mainland-only**.
2. Add under the matching category in `apps-direct-domains.list`.
3. Open a one-app-per-PR PR.

## License

MIT
