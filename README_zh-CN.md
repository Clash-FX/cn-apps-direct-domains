# cn-apps-direct-domains

[English](README.md) | [简体中文](README_zh-CN.md)

社区维护的国内常用 app / 服务**域名直连**规则集，采用 mihomo / Clash classical rule-provider 格式。

这是 [`Clash-FX/cn-apps-direct`](https://github.com/Clash-FX/cn-apps-direct) 的**域名版补充**。

| 属性             | `cn-apps-direct`                       | `cn-apps-direct-domains`（本仓库） |
|------------------|----------------------------------------|------------------------------------|
| 规则类型         | `PROCESS-NAME,...`                     | `DOMAIN-SUFFIX,...`                |
| 规则模式可用     | ❌（拿不到进程名）                     | ✅                                 |
| 增强模式（TUN）可用 | ✅                                   | ✅                                 |
| 匹配精度         | 按 app 精确匹配（不会误伤）            | 按域名（覆盖 app + 共享基础设施）  |
| 适合谁           | 已经开了增强模式的用户                 | 规则模式用户 / 增强模式补充        |

## 为什么有两个仓库

`PROCESS-NAME` 规则精度高，但**只有增强模式（TUN）才能用** —— 因为 mihomo 必须接管 socket 才看得到发起请求的进程名。如果你是传统的系统代理（规则模式），mihomo 只看得到目标域名和 IP，`PROCESS-NAME` 规则会静默失效。

本仓库用 `DOMAIN-SUFFIX` 实现同样的"让国内常用应用直连"意图，但**不依赖增强模式**，规则模式下也工作。

## 使用方式

### 通过 ClashFX 使用

ClashFX 计划加入一个"国内域名直连"开关，自动注入本规则集到生成的配置里。进度跟踪：[Clash-FX/ClashFX#104](https://github.com/Clash-FX/ClashFX/issues/104)。

在那之前，用下面"独立使用"的方法。

### 独立使用（任意 mihomo / Clash 客户端）

在你的 `config.yaml` 加入：

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
  # ... 然后是你原来的规则
```

## 收录原则

为了避免误伤海外用户/海外业务，本列表**只收录纯国内服务的域名**：

- ✅ `weixin.qq.com`、`music.163.com`、`bilibili.com` — 国内独有。
- ❌ `larksuite.com`（Lark 国际版）、`tiktok.com`（TikTok 国际版） — 这些是有海外用户需要走代理的合法场景，不能强制直连。
- ❌ `apple.com`、`microsoft.com` — 全球服务，由用户在主规则里自行决策。

如果一个 app 同时有国内和海外业务（比如飞书 / Lark），**只收录 `.cn` / 大陆独有**的那部分域名。

## 为什么没有 IP 规则

本列表刻意不包含 `IP-CIDR` 规则。原因：
- 域名规则更易审查
- CDN 拓扑变更时不会突然失效
- 跟 fake-IP DNS 模式（很多用户在用）兼容更好

如果需要 IP 级别的"中国流量直连"，把本列表跟 `GEOIP,CN,DIRECT` 一起用即可，mihomo 会正确处理优先级。

## 如何贡献

欢迎 PR，见 [CONTRIBUTING.md](CONTRIBUTING.md)。简单说：

1. 确认这个域名**只服务国内**。
2. 在 `apps-direct-domains.list` 对应分类下加规则。
3. 一个 PR 加一个 app。

## 许可证

MIT
