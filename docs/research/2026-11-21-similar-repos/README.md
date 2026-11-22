# Similar Open-Source Projects

Researched 2026-11-21. Candidate list from the bitdoze.com roundup of open-source Grok Bot
alternatives; stars, license and dates from the GitHub API the same day. Only OpenMausBot's code was
read; the rest are judged from their descriptions.

**Rule before borrowing code:** GPL-3 and AGPL-3 projects (openhuman, lorca, rerun) would put the
borrowing project under the same terms. Borrow ideas from those, not code.

## Same shape as MausBot (a roster of bots, each with a computer)

| Repo | Stars | License | Created | What to take from it |
|---|---|---|---|---|
| [elie222/rakazo](https://github.com/elie222/rakazo) | 9,385 | Apache-2.0 | 2026-08-13 | Closest twin, as a self-hosted server instead of a desktop app; compare its shared vs per-bot computer design |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | 13,124 | MIT | 2026-08-17 | Slack-style AI coworkers, each in a container, with a policy gateway and audit log; a template meant to be copied |
| [nanocoai/nanoclaw](https://github.com/nanocoai/nanoclaw) | 31,135 | MIT | 2026-01-31 | One container per agent, messaging front end, no UI; the smallest readable version of the pattern |
| [nickvasilescu/orgo-teammates](https://github.com/nickvasilescu/orgo-teammates) | 279 | MIT | 2026-11-09 | Formerly grokbot-clone; too new to rely on |
| [egoist/lorca](https://github.com/egoist/lorca) | 380 | GPL-3.0 | 2026-09-18 | End-to-end-encrypted bots on paired computers; ideas only |
| [rerun-build/rerun](https://github.com/rerun-build/rerun) | 1,118 | AGPL-3.0 | 2026-10-29 | Business AI coworkers with watchable computers; ideas only |

## Building blocks

| Repo | Stars | License | Created | Why it matters |
|---|---|---|---|---|
| [trycua/cua](https://github.com/trycua/cua) | 32,742 | MIT | 2025-01-31 | The computer-control layer MausBot itself uses (`cua-driver`); the base if we ever build our own |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent) | 15,865 | Apache-2.0 | 2025-07-29 | Splits one big task across parallel agents on your machine |

## Single assistants (Hermes-style)

| Repo | Stars | License | Created | Notes |
|---|---|---|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 394,959 | MIT | 2025-11-24 | Lives in WhatsApp, Telegram, Slack; big plugin ecosystem. Previously run by the operator (an `openclaw` folder went to the Trash on 2026-11-13) |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | 42,786 | GPL-3.0 | 2026-02-18 | Lightweight assistant with memory and voice; approval before it touches Chrome or apps |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 265,132 | MIT | 2025-07-22 | See the evaluation file |

## Skipped

- [paperclipai/paperclip](https://github.com/paperclipai/paperclip) (115,614 stars, MIT): an org chart with
  budgets and approvals over existing agents. That is the governance-layer product shape the operator
  rejected on 2026-11-09.

## Reading list if this goes further

1. NanoClaw, for the container-per-agent pattern.
2. OpenBot's policy gateway, for approving risky actions without clicking every one.
3. Cua, as the base for anything we build ourselves.
