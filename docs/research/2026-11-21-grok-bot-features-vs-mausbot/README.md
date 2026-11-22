# Grok Bot Features vs MausBot

Researched 2026-11-21, before 10:26 CT from xAI's launch page and MausBot's own comparison page.

## Was MausBot built from Grok Bot?

Yes, in shape, not in jobs. It started life as "OpenGrokBot", the repo was created 2026-08-11 (the
day Grok Bot was announced), and its own page says it "takes the same shape, a messaging app where
every contact is an agent." It copies the container (roster of bots, a computer, routines, group chats,
approvals). It does not copy or target the jobs xAI advertises.

## What xAI says Grok Bot does (x.ai/news/introducing-grok-bot)

- Its own cloud computer, so jobs continue while you are away. One computer per account, shared by all bots.
- Signs in to websites and apps, including ones with no API or MCP.
- Multi-step jobs end to end; comes back only for approval (Auto Review).
- Several bots in parallel; a "chief of staff" bot coordinates specialists; group chats of 2 to 6 bots.
- "Teach a task": learns a workflow from a demonstration and saves it as a routine. Up to 50 routines per bot.
- Separate usage: work handed to a bot "won't count against your existing usage."
- Example jobs, all business operations: sales outbound (research accounts overnight, score contacts,
  draft emails and LinkedIn messages), demo readiness, CRM and pipeline hygiene with a Monday
  scoreboard, account follow-up, invoices from Gmail, bug repro handed to a debugging bot.
- Beta on desktop and iOS. Plan names and prices conflict across xAI and MausBot pages; not settled.

## What MausBot's comparison page admits it lacks (mausbot.com/blog/grok-bot-vs-openmausbot)

- No "Teach a task": routines are set up by hand.
- The desktop app stops when the computer sleeps; overnight needs a server or a paid Cloud plan.
- No ready-made bot marketplace, no Microsoft Teams bots, no bots joining video calls; team bots are Slack only.

## What MausBot does differently

- 16 engines (Claude Code, Codex, Grok and more), model chosen per bot; Grok Bot has no model picker.
- Runs on your machine or server; data in `~/.openmausbot`. Free under Apache 2.0 except `enterprise/`.
- **New bots default to Full access.** Approvals are set per bot.
- No AI usage included: it spends your own subscription's limits, where Grok Bot's usage is separate.

Sources:
- [Introducing Grok Bot (xAI)](https://x.ai/news/introducing-grok-bot)
- [Grok Bot vs OpenMausBot (mausbot.com)](https://mausbot.com/blog/grok-bot-vs-openmausbot)
- [VentureBeat on Grok Bot](https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month)
