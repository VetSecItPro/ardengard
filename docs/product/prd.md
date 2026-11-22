# Ardengard version 1: product requirements

Status: Draft for approval. Updated 2026-11-22. Generated from prd.json; do not edit by hand.

Working name: Ardengard (chosen 2026-11-22)

## Problem

- Grok Bot, Muse, dots and Cue sell a team of AI coworkers with their own computers, but they are closed, run on the vendor's cloud and hold your data.
- The open-source alternatives (OpenMausBot, OpenClaw, Hermes) are young, rebuild their own chat apps, and shipped serious security holes in 2026.
- Builders in your community want a team of agents they can run themselves, understand, and trust, without writing a chat app.

## Users

- **You:** Build it in public, run it for demos and content, show what works and what does not, with real numbers.
- **Builders in your community:** Install one package on their own server, get a safe working bot team in an hour, and extend it with their own skills.

## Goals

- One install brings up a Buzz workspace with at least one Claude Code bot that answers in channels and threads.
- Bots learn through skill files and remember through plain-file memory they can show and forget.
- Every risky action waits for approval; safe defaults ship on; nothing listens on the public internet.
- Every job records its real value: time you estimated against time you spent reviewing and fixing.
- A newcomer goes from a fresh server to a first finished job in under one hour by following the docs.

## Not in version 1

- Our own chat app or phone app (Buzz and Telegram cover version 1).
- Bot email addresses, phone numbers, wallets or payments.
- WhatsApp, iMessage or Signal channels.
- Teaching by demonstration, a knowledge graph, agent-to-agent (A2A) links, multi-tenant hosting.
- Training or fine-tuning a model.

## Architecture

We do not build a chat app or an agent loop. Buzz provides the workspace; Buzz's own connector runs Claude Code as a Buzz member; our code is the layer that makes bots safe, useful and measurable.

| Part | Role | Source | Ours |
|---|---|---|---|
| Buzz relay | Workspace: channels, threads, DMs, search, signed audit log. | Official image ghcr.io/block/buzz pinned by release and digest, with Postgres, Redis and MinIO | no |
| buzz-acp | Connects a bot to Buzz: listens for mentions, prompts the agent, posts replies. Defaults to answering only its owner. | block/buzz, Apache 2.0 | no |
| claude-agent-acp | Runs Claude Code as an ACP agent that buzz-acp can drive. | agentclientprotocol/claude-agent-acp, Apache 2.0 | no |
| Bot definitions | One folder per bot in git: instructions, skills, tools, model, permissions. | Ours | yes |
| Gatekeeper | Permission broker for every tool call: allow lists, never-delegate list, untrusted-content quarantine, one-writer rule, caps, kill switch. | Ours, using Claude Code hooks and permission callbacks | yes |
| Memory server | MCP server over markdown fact files and SQLite full-text search: add, update, delete or skip; scopes; unverified flag; nightly tidy. | Ours | yes |
| Bot computer | A sandboxed Linux desktop with a browser, driven through Cua, for website work. | trycua/cua, MIT | no |
| Doorbell | Telegram bot that answers only you: short notices and approve or deny buttons; no sensitive content. | Ours, on grammY | yes |
| Value log and traces | Per-job estimate, review time, rework, cost and OpenTelemetry traces. | Ours plus a self-hosted trace viewer | yes |
| Installer | One Docker Compose stack with Tailscale, backups and update with rollback. | Ours | yes |

## Requirements

| ID | Area | Requirement |
|---|---|---|
| R1 | install | docker compose up on Ubuntu 24.04 starts Buzz, one bot and all its services; the server refuses to start on a public address. |
| R2 | roster | A bot appears in Buzz as a member with its own key, answers @mentions in channels, threads and DMs, and answers only its owner by default. |
| R3 | agents | Each bot is defined by a folder in git; a change runs the bot's tests before it goes live; one command rolls back. |
| R4 | skills | Bots load skill files in the Agent Skills format; a bot may propose a skill edit, which needs your approval and must pass the skill's tests. |
| R5 | memory | Bots read and write memory only through the memory server; every fact has source, date, scope and expiry; you can list, edit and forget facts. |
| R6 | context | Each turn gets the core profile, the task, retrieved facts and only the tools the job needs; long sessions end with a handoff note and restart fresh. |
| R7 | security | New bots start read-only with Ask on every action; irreversible actions always wait for you; a bot that read untrusted content cannot send or change settings in that turn. |
| R8 | security | Secrets are used through a broker and never enter a model's context, a transcript or a log. |
| R9 | teamwork | For any task exactly one bot writes; others may only advise. |
| R10 | reach | A Telegram bot that answers only your user ID sends notices and approve or deny buttons and never includes client names, money, health or credentials. |
| R11 | computers | A bot can use a sandboxed desktop with a browser for website work; you can watch it and take over. |
| R12 | durable | A job keeps a progress file, survives a restart and resumes; a job with no progress for 20 minutes is reported. |
| R13 | quality | Nothing a bot makes is sent to another person until a reviewer step marks it complete. |
| R14 | observe | Every job records a trace with steps, time, tokens and cost, viewable in a self-hosted viewer. |
| R15 | value | Every job records your estimate before and your review and fix time after; the scorecard shows wins and losses. |
| R16 | security | A Pause all control stops every bot and revokes sessions; daily caps on usage and messages per bot. |
| R17 | data | Nightly encrypted backups to storage you own; one command restores, exports everything, or deletes a scope. |
| R18 | community | Apache 2.0 license, SECURITY.md, signed releases with a changelog, docs that take a newcomer to a first job in under an hour. |

## Non-functional

- Runs on a 4 vCPU, 16 GB server with one shared bot desktop; the minimum is measured in phase 0.
- Reachable only over Tailscale; no public ports.
- Every dependency, image, MCP server and skill pinned by version and digest.
- Files 0600 and folders 0700; the build fails on readable secrets.
- /sec-ship on every PR; /redteam against a local instance before each release.

## Success measures

- Install to first finished job: under 60 minutes for a newcomer following the docs.
- Benchmark jobs used without rework: at least 3 of 5 by release 1.
- Actions that ran without required approval: zero, tested every release.
- Your review and fix time below your own estimate on at least half of benchmark runs.

## Risks

| Risk | Plan |
|---|---|
| Buzz is a developer preview; approval gates and phone apps are unfinished. | Phase 0 spike; pin a release; fallback interface from the mockup if Buzz fails the check. |
| How buzz-acp handles Claude Code permission requests is unknown. | Phase 0 spike decides whether approvals flow through Buzz, Telegram or both. |
| Bots share your Claude plan limits. | Daily caps per bot; a separate account or API key decided in phase 0. |
| Community members run it carelessly and expose it. | Refuse public addresses, safe defaults, plain-language security docs. |
| It feels useful but is not. | Value log and benchmark from the first job; publish losses too. |

## Open questions

- Separate Claude account or API key for bots, or your subscription with caps?
- Accept outside pull requests from day one, or publish as a reference build first?
- Workflow engine (Temporal, Hatchet) or a SQLite job table for version 1?
- Which trace viewer (Langfuse, OpenLIT, Opik)?
