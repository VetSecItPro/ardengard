# Ardengard version 1: build plan

Status: Draft for approval. Updated 2026-11-22. Generated from plan.json; do not edit by hand.

## Rules

- Nothing in a phase starts until the PRD is approved and the previous phase's exit check passes.
- Every task ships with its tests; every phase ends with /smoketest and a demo you can film.
- One work block is one branch and one PR through /gh-ship.
- Each phase updates the discussion log and the scorecard.

## P0 Spikes: prove the unknowns

Goal: Answer the questions that could change the design before any real code.

Exit check: Each spike has a written result in the discussion log and the PRD is updated.

| Task | What | Done when | Requirements |
|---|---|---|---|
| P0.1 | Run the Buzz Compose stack (pinned release) on a test server and record memory, CPU and disk at idle and with one bot. | Numbers recorded; minimum server size set in the PRD. | R1 |
| P0.2 | Connect Claude Code to Buzz with buzz-acp and claude-agent-acp; one bot answers an @mention in a thread. | A screen recording of the reply; setup steps written down. | R2 |
| P0.3 | Find out what happens to Claude Code permission requests under buzz-acp (shown, auto-denied or auto-approved). | Decision recorded: approvals flow through Buzz, Telegram, or our gatekeeper hook. | R7 |
| P0.4 | Log Claude Code in on a headless server and measure how bot usage counts against your plan. | Decision recorded: your subscription with caps, or a separate account or API key. | R16 |
| P0.5 | Drive a Cua desktop container from Claude Code over MCP: open a site, read a page, take a screenshot. | Working example committed; resource cost noted. | R11 |
| P0.6 | Drive a browser from Claude Code with Browser Harness inside the bot's desktop container; run one real website task and compare speed and token use with Cua screenshots. | Decision recorded: Browser Harness, Cua, or both, for website work. | R11 |

## P1 Foundation

Goal: A new repo and a safe one-command stack with nothing yet clever in it.

Exit check: Fresh Ubuntu 24.04 server to running stack with one command, reachable only over Tailscale, backups running.

| Task | What | Done when | Requirements |
|---|---|---|---|
| P1.1 | Pick the server for development; create the ardengard repo under a GitHub organization (ardengard-dev or ardengardhq; github.com/ArdenGard is a personal account) with /repo-bootstrap (CI gate, tests, Apache 2.0 LICENSE, SECURITY.md, CHANGELOG); register ardengard.dev. | Repo public or private as decided; CI green on an empty test. | R18 |
| P1.2 | Write the Compose stack: Buzz relay pinned by digest, Postgres, Redis, MinIO, Tailscale sidecar, our bot service placeholder container. | docker compose up works; a test proves no port listens publicly. | R1 |
| P1.3 | Add the startup guard that refuses a public address and the file-permission check (0600 and 0700). | Tests fail on a public bind and on a readable secret file. | R1, R8 |
| P1.4 | Add nightly encrypted backups (restic for files, Postgres dump, SQLite with Litestream) and a restore command. | A restore onto a clean server is tested and passes. | R17 |
| P1.5 | Add update with automatic backup and rollback on failed health check. | A deliberately broken update rolls back by itself. | R17 |

## P2 First bot

Goal: One Chief of Staff bot that lives in Buzz, defined in git, safe by default.

Exit check: You message the bot in Buzz, it answers, and every action it attempts asks first.

| Task | What | Done when | Requirements |
|---|---|---|---|
| P2.1 | Define the bot folder format (instructions, skills, tools, model, permissions) and the Chief of Staff bot. | Format documented; the bot loads from its folder. | R3 |
| P2.2 | Wire the bot into Buzz through buzz-acp with owner-only answers and its own key. | Bot answers mentions, threads and DMs; strangers are ignored (tested). | R2 |
| P2.3 | Load skill files in the Agent Skills format; start with two of your existing skills. | The bot uses a skill on request; skill tests pass. | R4 |
| P2.4 | Add bot tests and one-command rollback to the last good version. | A bad edit fails its tests and is not deployed; rollback works. | R3 |
| P2.5 | Start the value log: estimate before, review and fix time after, used without rework yes or no. | Every job produces a value record. | R15 |

## P3 Gatekeeper and doorbell

Goal: Approvals, limits and the phone doorbell, before bots can do anything real.

Exit check: Red-team tests show no action runs without its approval, and you can approve from Telegram.

| Task | What | Done when | Requirements |
|---|---|---|---|
| P3.1 | Build the gatekeeper: per-bot allow lists, the never-delegate list, read-only default, Ask on everything. | Tests try each action type without approval and all are blocked. | R7 |
| P3.2 | Untrusted-content quarantine: a turn that read web, email or bot content loses send and settings rights. | A prompt-injection test page cannot make the bot send anything. | R7 |
| P3.3 | Secrets broker: logins filled at use time, never in context, transcripts or logs. | A test searches all logs and transcripts for the secret and finds none. | R8 |
| P3.4 | Pause all, per-bot daily caps on usage and messages, and the one-writer rule per task. | Pause stops a running job within seconds; caps trip in tests. | R16, R9 |
| P3.5 | Telegram doorbell: owner-only bot with approve and deny buttons and the content rule. | An approval from the phone unblocks a job; a test confirms no sensitive fields are sent. | R10 |

## P4 Memory and context

Goal: Bots that remember correctly and see only what they need.

Exit check: A bot remembers a fact across days, shows where it came from, and forgets it on request.

| Task | What | Done when | Requirements |
|---|---|---|---|
| P4.1 | Memory server (MCP) over markdown fact files with front matter and SQLite full-text search. | Read, write, search and forget work through MCP; files are readable by you. | R5 |
| P4.2 | Write pipeline: add, update, delete or skip, with history; source, date, scope and expiry on every fact. | A contradicting fact updates the old one instead of duplicating it (tested). | R5 |
| P4.3 | Unverified flag for facts from untrusted sources; they cannot change instructions or permissions. | A poisoned-memory test fails to change bot behavior. | R5, R7 |
| P4.4 | Context recipe per bot: core profile, task, retrieved facts, trimmed tools; handoff note and fresh restart for long sessions. | Token use per turn measured before and after; quality holds on benchmark jobs. | R6 |
| P4.5 | Nightly tidy: merge duplicates, expire stale facts, propose deletions for approval. | Nightly report lists changes; nothing deleted without approval. | R5 |

## P5 Computer and long jobs

Goal: A Researcher bot that works through websites on its own desktop, for hours if needed.

Exit check: The prospect-list benchmark job runs overnight, survives a restart, and finishes.

| Task | What | Done when | Requirements |
|---|---|---|---|
| P5.1 | Add the Researcher bot with a shared Cua desktop and browser; you can watch and take over. | The bot completes a multi-page website task with screenshots in the thread. | R11 |
| P5.2 | Job runner with progress file, retries, resume after restart and a 20-minute stall alert. | Killing the server mid-job and restarting resumes the job. | R12 |
| P5.3 | Reviewer step: a separate pass checks output before anything goes to a person. | Incomplete output is sent back, not delivered (tested). | R13 |
| P5.4 | Writer bot and the one-writer handoff from Researcher to Writer. | A two-bot job finishes with a single writer. | R9 |

## P6 Observe and harden

Goal: See everything the bots do, and attack it before anyone else does.

Exit check: Traces for every job, a clean /sec-ship, a passing /redteam, and a benchmark scorecard.

| Task | What | Done when | Requirements |
|---|---|---|---|
| P6.1 | OpenTelemetry GenAI traces for every step, sent to the chosen self-hosted viewer; cost and time per job. | Any job can be opened step by step. | R14 |
| P6.2 | Benchmark suite: 5 standing jobs rerun after every change, with the value log. | Benchmark report generated per release. | R15 |
| P6.3 | Red team: prompt injection, tool misuse, memory poisoning, side doors around approvals (promptfoo, garak, /redteam). | Every finding fixed or recorded; zero approval bypasses. | R7, R13 |
| P6.4 | /sec-ship full pass; pin and scan every dependency, image, MCP server and skill. | No open high or critical findings. | R18 |

## P7 Release to the community

Goal: Something a newcomer can install safely, and the story of building it.

Exit check: A newcomer installs it from the docs and finishes a first job in under an hour, and release 1 is published.

| Task | What | Done when | Requirements |
|---|---|---|---|
| P7.1 | First-run setup: creates one safe example bot and explains each permission it asks for. | A clean install reaches a working example bot with no manual edits. | R18 |
| P7.2 | Docs site for people who have never run a server; safe defaults and risks explained plainly. | A newcomer test run under 60 minutes. | R18 |
| P7.3 | Signed release with changelog; the install refuses versions with known advisories. | Release 1 published and verified from a clean machine. | R18 |
| P7.4 | You run release 1 yourself long enough to film the demo. | Demo recorded; problems found are fixed before sharing. | R15 |
| P7.5 | Public scorecard and build-log posts drafted through /post for your approval. | Scorecard page live; posts in Desk for approval. | R15 |
