# MausBot Experiment Plan

Drafted 2026-11-21 10:08 CT. Status: **draft, not approved.** Live document.

## The question

Can a self-hosted OpenMausBot do the jobs I would pay xAI for Grok Bot to do, well enough and with
little enough upkeep that I would keep using it after two weeks?

The honest control is not Grok Bot (we are not paying for it). It is **Claude Code as I already use
it.** Every job is also judged against "would I just have done this in Claude Code?" If the answer is
always yes, the trial has answered the question too.

## The box: one idle 2 vCPU, 8 GB VPS

- Specs: 2 vCPU, 8 GB RAM, 100 GB NVMe.
- MausBot's minimum is 2 cores, 4 GB, 20 GB disk; 8 GB suggested. **This size meets it.**
- Candidates: two idle servers of this size; which one is in `private/`.

### Memory budget (estimates, to be measured in phase 1)

| Item | Estimate |
|---|---|
| Ubuntu, Docker, Tailscale | about 1 GB |
| MausBot server and Caddy | about 1 GB |
| Each active Claude Code process | 0.3 to 0.5 GB |
| One shared bot desktop (default limit) | 4 GB |
| **Total with 2 to 3 bots working and one desktop** | **about 7 GB of 8** |

- Run the desktop in `shared` mode (the default), never `per-bot`: a second desktop does not fit.
- **The 2 vCPUs are the real squeeze.** A desktop running a browser will slow everything else down.
  If the scorecard shows that, the answer is "fine on a 4 or 8 vCPU server", not "MausBot is bad".

## Phases

### Phase 0: prepare the box (needs operator)

1. Inventory the idle servers: IP, OS, what is running, anything worth keeping.
2. Operator picks the box and gives a **go to wipe it**. Take a provider snapshot first if anything
   on it might matter.
3. Reinstall Ubuntu 24.04. Add an SSH key and a Mac `~/.ssh/config` entry. Install Tailscale.
4. Claim the box on the session board before touching it; release it at teardown.

### Phase 1: install (about 1 hour)

1. Run the installer with `--check` first and save the output in this folder.
2. Install with **path C, Tailscale only**: no domain, no public ports, reachable from the Mac and
   phone on the tailnet. The Mac already has Tailscale installed.
3. Pin the release version and write it down here.
4. Log in the `claude` command-line tool on the server. **Note: this uses my Claude subscription, so
   every bot shares the usage limits my Claude Code work runs on.** That is a real cost of the trial.
5. Phone access: install MausBot's web app from the Tailscale HTTPS address (Safari, Add to Home Screen) and pair it.
   Not the hosted MausBot Relay: it is end-to-end encrypted, but it needs a MausBot account and a third-party service,
   and the trial stays Tailscale-only. The native App Store app pairs by QR with the desktop app or MausBot Cloud;
   for a self-hosted server it needs that relay. Note: alerts arrive only while the app is connected, so phone push
   is weak; Telegram stays the doorbell.
6. Run the server's own self-check (it confirms a bot cannot read `config.json`) and record the result.
7. Measure idle memory and CPU, then again with one bot working and the desktop up. Replace the
   estimates above with the numbers.

### Phase 2: use it for two weeks

- 2 to 3 bots, each with a clear job (env #783 picks the jobs).
- Shared Full access **off**. **New bots default to Full access: set every bot to Ask when it is created.**
- **No real Gmail, Slack or GitHub connections.** If a job needs a connected app, use a throwaway
  account. Reason: the open approval bypass in its SECURITY.md, and plaintext MCP secrets.
- Log every run in `trial-log.md`: date, job, result, time, approvals clicked, what I had to fix.

### Phase 3: verdict and teardown

- Fill in the scorecard, write the verdict in `discussion-log.md`.
- Keep it, move it to a bigger box, or tear it down (`install.sh --uninstall`, then wipe the box).

## Draft test jobs (operator picks 3 to 5, env #783)

**Not coding, and not plain research.** MausBot's bots are Claude Code underneath, so for those jobs
the brain is identical and Claude Code at the desk wins (2026-11-21, before 10:26 CT). The jobs must test what
the environment adds: always on with the Mac closed, phone-first chat, a desktop with a browser it
clicks through, schedules, several standing bots. Guesses below; replace with the real reasons I wanted Grok Bot.

1. **Ask from the phone away from the Mac,** get a finished result back while the laptop is closed.
   Tests always-on plus the phone app. Overlaps with Claude Code Remote Control: compare the two.
2. **A website with no API:** log in to a site, click through, pull or fill something (a test account).
   Tests computer use on its desktop, the part Grok Bot sells hardest. Claude Code can only partly do
   this through Playwright at the desk.
3. **A proactive routine:** a bot that watches something on a schedule and messages me only when it
   changes. Tests routines and notifications. Overlaps with cloud `/schedule` routines: compare.
4. **A standing bot with its own memory:** one bot kept for one ongoing topic for two weeks, picked up
   from the phone. Tests whether a persistent persona beats a fresh Claude Code session.
5. **A two-bot handoff:** one bot gathers, another turns it into a one-page result, without me
   steering between them. Tests bot-to-bot coordination.
6. **A real job in xAI's own example category (sales research):** build a prospect list from a public registry, filling name, city, size,
   platform and contact columns by working through websites. Closest match to Grok Bot's advertised
   "research accounts overnight, score contacts" job, and it is work I already need done.

## Scorecard

| Measure | Pass |
|---|---|
| Jobs finished without me fixing anything | 3 of 5 or better by the end of week 2 |
| Upkeep (updates, restarts, re-logins) | Under 1 hour a week |
| Effect on my Claude usage limits | No days where Claude Code work was blocked by bot usage |
| Better than doing it in Claude Code | At least 2 jobs where I would honestly choose MausBot |
| Security | No action ran without its approval card |

## Kill criteria (stop early if any is true)

- The installer's checks or the self-check fail on a clean Ubuntu 24.04 and a rerun does not fix it.
- Any action runs without its approval card.
- After week 1, fewer than 2 jobs succeed unaided.
- Bot usage blocks my own Claude Code work.

## Cost

- Box: already paid; no new spend.
- Claude usage: from my existing subscription (see phase 1, step 4).
- Time: about 2 hours setup, then a few minutes a day logging runs.
- Grok Bot comparison price: open, check xAI's pricing page (see `research/2026-11-21-grok-bot-and-ondrej-video.md`).
