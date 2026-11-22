# OpenMausBot Evaluation

Researched 2026-11-21 by reading the GitHub repo through the GitHub API (metadata, contributors,
commits, releases, README, SECURITY.md, LICENSING.md, CLA.md, docs and server code).
Nothing was installed or run.

## Verdict at the time of writing

Not ready to replace anything that touches real accounts. Fine to trial in a sandbox: a spare server,
no connected Gmail or Slack, shared Full access off.

## What it is

- Repo: [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), site openmausbot.com.
  Formerly named OpenGrokBot. Not affiliated with xAI.
- An Electron desktop app (TypeScript, React 19) plus a small Node server. It works like a messaging
  app: a list of bots you chat with, each with its own personality, model, computer and connected apps.
- Bots run on the `claude`, `codex` or `grok` command-line tools, logged in with your own
  subscriptions. No proxy in the middle.
- Connected apps (Gmail, Slack, GitHub, Notion, Linear, 500+) come through Composio.
- Risky actions (shell commands, file edits) show up as Allow / Deny cards in the chat.
- Data lives in `~/.openmausbot` (or `/opt/openmausbot/data` on a server).

## Health (2026-11-21)

- Created 2026-08-11. Latest release v0.1.175 (2026-11-21). Five releases between 2026-11-17 and 2026-11-21.
- 26,278 stars, 3,745 forks. Star surge came from GitHub trending around 2026-11-07.
- 1,225 open issues, 40 with the bug label. 311 open pull requests.
- 944 pull requests from people other than the maintainer merged since 2026-11-01.
- Contributors: milind-soni about 6,981 commits; next is 793. Bus factor of one.
- Sponsors in the README: boat.dev (cloud computers) and ModelGo (inference).
- Unrelated crypto tokens use its name; the README disowns them.

## License

- Core: Apache 2.0. Fork, modify and use commercially; keep LICENSE and NOTICE.
- `enterprise/`: source-available, not open source. Production use needs a paid key; hosting for
  others needs a partner agreement. Delete the folder and the open-source edition remains.
- Contributing outside `enterprise/` needs no CLA. Inside it needs the CLA.
- The project's own rule: customizations belong "as data and configuration, never as a fork."

## Security notes from its own SECURITY.md

- **Known open gap:** on a shared or hosted workspace, a bot's shell can post into an existing
  Full-access Slack thread "and get Full-access work done without a card." Planned fix: a worker-only
  relay token. Not shipped as of 2026-11-21.
- Some secrets are plaintext on every install: OpenCode provider keys, per-engine environment values,
  MCP environment and header values, `mcp-oauth.json`.
- A bot with Full access runs as you and can read your saved session file.
- The server listens on 127.0.0.1 only; mutations need a per-launch capability or a paired session.

## What "each bot has its own computer" means

Mostly containers, not virtual machines, and by default all bots share one.

| Option | What it is | Where it runs |
|---|---|---|
| Local VM | A Docker or Podman container with a Linux desktop (Cua) | Your machine; on a Mac, inside Docker's one Linux VM |
| Cloud ("Boat") | A remote Linux desktop | boat.dev, the sponsor. Price not documented in what was read |
| Your own VPS | The same desktop container, placed over Docker's SSH transport | A Linux server you own |
| This computer | Your real desktop through the bundled `cua-driver` | Your machine, after an explicit opt-in |

- Sharing modes (`server/local-vm-settings.ts`): `shared` (default, one desktop for all bots),
  `per-bot`, `pool` (capped set of desktops). Idle desktops stop after 480 minutes by default.
- Limits (`server/container-limits.ts`): 2 CPUs and 4 GB each by default, range 1 to 64 CPUs and
  2 to 128 GB. Memory and swap share one limit, so there is no swap: past the limit the kernel kills
  processes. PID limit 4,096.
- The Local VM needs the Docker socket; the bot sandbox refuses to mount it because that would be
  root-equivalent.
- On a server install, each bot turn runs inside a bubblewrap sandbox (`docs/bot-box.md`): no view of
  the server's data folder or other bots, loopback-only network, outbound only through a filtering
  proxy that refuses private and cloud-metadata addresses. Measured cost about 5 ms and 3 MB per box.

## Server install requirements (`docs/deploy-vps.md`)

- Ubuntu 22.04 or 24.04, x86-64, 2 cores or more, 4 GB RAM (8 GB suggested), 20 GB free disk.
- Docker 24+ with the Compose plugin, not rootless. User namespaces and AppArmor on.
- One-command installer (`deploy/install.sh`) checks everything first and changes nothing until all
  checks pass. `--check` runs the checks only. It sends no telemetry.
- Three ways in: A, public tunnel through an OpenMausBot account; B, your own domain with Caddy on
  ports 80 and 443; C, Tailscale only (`serve --tailscale`), nothing public.
- Runs fully on a server: engine CLIs, chats, rooms, bot-to-bot work, routines, connected apps, MCP
  servers, webhooks, computer use on cloud or container computers, the web UI.
  Needs the desktop app: dictation and controlling the server's own desktop.

## Compared with Hermes Agent (NousResearch/hermes-agent)

| | Hermes Agent | OpenMausBot |
|---|---|---|
| Age | Since 2025-07-22 | Since 2026-08-11 |
| Version | v0.23.3 | v0.1.175 |
| Stars | 265,132 | 26,278 |
| Top contributors | teknium1 29,791; then 5,841, 4,582, 2,381 | milind-soni 6,981; then 793 |
| License | MIT | Apache 2.0 plus a paid `enterprise/` folder |
| Shape | One agent with memory and skills, on a server, reached through messaging apps | A team of bots in a desktop app, each with a computer and approval cards |

Hermes is far more mature. OpenMausBot is better at using an existing Claude subscription, approval
cards and per-bot computers. Note: the operator retired his own Hermes deployment on
2026-11-13.
