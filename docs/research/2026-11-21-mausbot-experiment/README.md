# MausBot Experiment

Is OpenMausBot (open source, self-hosted) good enough to replace paying xAI for Grok Bot?
This folder holds everything about that question so nothing is lost between sessions.

Started 2026-11-21 10:06 CT. Backlog rows: env #780 to #783 and #752 in
`../environment-improvement-backlog.md`.

## Status

- **Research:** done, 2026-11-21 (see `research/`).
- **Plan:** drafted, 2026-11-21 (`plan.md`). Not approved yet.
- **Install:** not started. Waiting on the operator: which test server, a go to wipe it, SSH access (env #782, #752).
- **Agent Wishlist (design workbook):** 12 design areas, 78 ideas, security and memory design, reference repos per area,
  and the discussion log, published 2026-11-21 (`wishlist/`, artifact link below). Decided areas are pruned to the decision.
- **Test jobs:** waiting on the operator to pick 3 to 5 (env #783, draft list in `plan.md`).

## Files

| File | What it is |
|---|---|
| `plan.md` | The experiment: box, install path, test jobs, scorecard, kill criteria, teardown |
| `discussion-log.md` | Dated log of the questions asked, answers given and decisions made |
| `research/2026-11-21-openmausbot-evaluation.md` | What OpenMausBot is, its health, security notes, how its "computers" work |
| `research/2026-11-21-similar-repos.md` | Other open-source projects in the same space and what to borrow from each |
| `research/2026-11-21-grok-bot-and-ondrej-video.md` | Grok Bot pricing (unconfirmed) and what David Ondrej's video actually covers |
| `research/2026-11-21-grok-bot-features-vs-mausbot.md` | What Grok Bot does per xAI, what MausBot copied, and what it admits it lacks |
| `wishlist/ideas.json` | **Source of truth** for the workbook: design areas, ideas, security, memory and reference repos |
| `wishlist/build_wishlist.py` | Builds `wishlist/wishlist.md` and `artifacts/agent-wishlist.html` from `ideas.json`; run after any edit |
| `artifacts/agent-wishlist.html` | The Agent Wishlist page, published at https://claude.ai/artifact/6z3iQwNWjHH9zJghwSj9s9 (republish this same path to update) |
| `mockups/bot-workspace-v1.html` | Clickable UI mockup of our bot workspace (open in Chrome); example data only |

## Rules for this folder

- Research files are dated and not rewritten later; a newer finding goes in a new dated file.
- `plan.md` and this README are live documents: update them as the trial moves.
- Every decision goes in `discussion-log.md` with a Central time stamp.
