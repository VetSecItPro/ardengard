# MausBot Experiment Discussion Log

Newest entries at the bottom. Central time on every entry.

## 2026-11-21 (session before this folder existed, condensed)

- **Asked:** is OpenMausBot a good replacement for Grok Bot? **Answer:** not ready for real accounts;
  three months old, one main maintainer, an approval bypass its own SECURITY.md lists as open. Fine to
  trial in a sandbox.
- **Asked:** what did David Ondrej's video say? **Answer:** he did not review it; his 2026-11-15 video
  builds his own clone, SuperBot (25 commits, one day of work). Transcript not checked (YouTube 429).
- **Asked:** can we use it and improve on it? **Answer:** yes under Apache 2.0, except `enterprise/`.
  Do not fork: it ships several releases a week. Run it unmodified, customize through config, engines
  and skills, and send fixes upstream.
- **Asked:** is it better than Hermes? **Answer:** Hermes is far more mature; MausBot is better at
  reusing a Claude subscription, approval cards and per-bot computers. Raised that an earlier Hermes bot (Hermes) was
  retired 2026-11-13 for being unwanted, and this is the same category.
- **Asked:** what does "its own computer" mean? **Answer:** a Docker container with a Linux desktop,
  shared by all bots by default, 2 CPUs and 4 GB each with no swap.
- **Asked:** what similar repos can we draw from? **Answer:** see `research/2026-11-21-similar-repos.md`.
  Read NanoClaw, OpenBot's policy gateway and Cua; skip Paperclip.

## 2026-11-21 10:06 CT

- **Asked:** would a small 2 vCPU, 8 GB server be enough to see how good it is, since I do not want to pay X for Grok Bot?
  What would make it a worthwhile experiment? Set up a folder to keep it all.
- **Answer:** yes, a 2 vCPU, 8 GB server meets the minimum; run one shared desktop, 2 to 3 bots. CPU
  is the tight part. Plan in `plan.md`. The real control is Claude Code, not Grok Bot.
- **Decisions made by Claude, overrule if wrong:**
  - Tailscale-only access (path C): nothing public on the box.
  - No real Gmail, Slack or GitHub connections during the trial.
  - Folder is tracked in git (it is research about this experiment, like `aios-icp/`).
- **Waiting on the operator:** which test server and a go to wipe it (env #782, #752); the 3 to 5 real
  jobs (env #783).

## 2026-11-21 (between 10:08 and 10:26 CT, first)

- **Asked:** are the test jobs coding, research, things Claude Code cannot do, or just a different environment?
- **Answer:** mostly a different environment. The bots are Claude Code underneath, so coding and plain
  research are not worth testing; Claude Code at the desk wins. What is new: a desktop with a browser
  the bot clicks through (sites with no API), always on with the Mac closed, phone-first chat,
  proactive routines, standing bots with their own memory, bot-to-bot handoffs. Some of that overlaps
  with Claude Code Remote Control, `/schedule` routines and Playwright, so each job compares against those.
- **Change:** `plan.md` draft jobs rewritten around those gaps; the comparison-research job was dropped.

## 2026-11-21 (between 10:08 and 10:26 CT, second)

- **Asked:** is MausBot based on the jobs Grok Bot reportedly does?
- **Answer:** on its shape, not its jobs. It began as OpenGrokBot on Grok Bot's launch day and copies
  the container. xAI's advertised jobs are business operations (sales outbound, CRM hygiene, invoices);
  MausBot targets none of them and admits it lacks Teach a task, video-call bots and a marketplace.
  Grok Bot's usage is separate from your plan; MausBot spends your Claude limits.
- **New facts for the plan:** MausBot bots default to Full access (set each to Ask). A real job close to
  xAI's sales example already exists: a prospect research list the operator already needs.
- Details: `research/2026-11-21-grok-bot-features-vs-mausbot.md`.

## 2026-11-21 10:27 CT

- **Asked:** match Grok Bot and improve on MausBot for everything; be comprehensive and imaginative, drawing on
  Grok Bot, Hermes, OpenClaw, Muse and the other repos. We paraphrase their ideas so we are not beholden to their
  code or licenses. A year in since OpenClaw, build a wishlist; maybe create our own and publish the journey.
  Put it in an artifact that is easy to read in the browser.
- **Answer:** 61-idea wishlist in 8 themes (`wishlist/ideas.json`), published as the Agent Wishlist artifact.
  Seven picks to start: teach by showing (#6), waiting questions on the phone (#47), trust ladder (#34),
  night-shift reflection (#15), overnight prospect research (#50), AIOS bridge (#45), bot email address (#18).
- **Pushback recorded:** fourth pass at the same idea (OpenClaw, an earlier Hermes bot, now this); that bot failed on
  use, not features, so the build is gated on the MausBot trial showing which jobs get handed off. The AIOS rule
  (build the system before chasing opportunities) counts this as system work only for ideas 45 to 52.
- **Decisions made by Claude, overrule if wrong:** "our own model" read as our own product on Claude, not a
  trained language model. Clean-room rules on the page: reuse ideas, never code, docs text, art or names;
  copyleft code not read at all; implementation works from the wishlist only.

## 2026-11-21 10:39 CT

- **Asked:** can we feed it skills so it learns from skills rather than watching the user?
- **Answer:** yes, and skills should be the main way bots learn. The bots run Claude Code, which already loads
  skill files, and MausBot keeps a skills folder per bot. A skill alone is instructions, not learning: the
  learning is the loop that edits the skill after each run, with tests so an edit cannot break it.
  Watching stays only for screen chores you cannot put in words, and it writes an ordinary skill file.
- **Change:** wishlist idea #6 reframed (a demonstration writes a skill); new ideas #62 to #65 (skills first,
  documents into skills, skills that improve after each run, test a skill before trusting it); pick #6
  replaced by #62. 65 ideas.

## 2026-11-21 10:42 CT

- **Asked:** do we think about cybersecurity and permissions? We will create our own repo, borrowing code patterns but
  doing our own thing, like David Ondrej did. Clarified: security of the bot code itself, what others warn about,
  over-permissive permissions.
- **Answer:** added a security model to the wishlist (version 5): 14 code lessons taken from real 2026 advisories in
  OpenClaw (exposed panels, CVE-2026-25253 WebSocket hijack, command injection, Claw Chain sandbox escape, .env
  override, insecure-auth flag), Hermes (world-readable secrets, DNS rebinding, path traversal, mutable MCP refs,
  prompt injection out of scope) and MausBot (Full access default, Slack approval side door), each with our rule
  and its OWASP agentic category; 10 runtime threats; 8 design rules; ideas #66 to #71. 71 ideas.
- **Pushback recorded:** Ondrej's SuperBot was a one-day build with no security work; the same approach is fine
  for ideas, but our repo does not ship without this model, /sec-ship on every PR and /redteam before releases.

## 2026-11-21 10:46 CT

- **Asked:** what to do for memory so the bots remember things; add it as features; which repos help with agent memory.
  Everything we discuss goes into the artifact so nothing is lost in chat.
- **Answer:** memory design added as a design area: five kinds of memory (working, core profile, facts, episodes, skills),
  a seven-step write pipeline, a build order (markdown files and SQLite full-text search first, meaning search second,
  a temporal knowledge graph only if needed), ideas #72 to #77, and 12 memory repos compared (mem0, Cognee, Graphiti,
  Supermemory, Letta, memU, MemOS, Honcho, Zep, Basic Memory, LangMem, A-MEM). Copyleft ones (Honcho, Basic Memory) are ideas only.
- **Pushback recorded:** wrong memory stated with confidence is the most common agent failure; more memory is not better
  memory; every memory is an attack surface (memory poisoning, idea #75). Your own Claude Code memory folder is already the
  version 1 design.
- **Asked:** have different sections for all of this, growing as we think, so we can start creating when the time comes.
- **Answer:** the page is now a design workbook with 12 design areas (scope, bots and chat app, computers, skills, memory,
  security, identity and reach, teamwork, AIOS, cost, quality, journey), each with status, decided items, open questions
  and linked ideas. This discussion log is rendered on the page.
- **Asked:** always research and name GitHub repos with code for each section, kept in the artifact for build time.
- **Answer:** a research pass for every area's reference repos is running (env #794); every new area gets its repos too.

## 2026-11-21 10:51 CT

- **Done:** reference repos added to 11 design areas (78 repos; memory keeps its own 12). A research agent proposed them; Claude
  rechecked every one with the GitHub API (all exist, none archived; google/gvisor is now gvisor/gvisor) and dropped two tiny
  ones (CogineBot, 10 stars; rakazo-android, 3 stars). Licenses are colored: green permissive, amber custom (check first),
  red copyleft (ideas only).
- **Standing rule:** every new design area gets researched reference repos, verified with the GitHub API, in the same pass.

## 2026-11-21 10:57 CT

- **Decided (operator):** Telegram is the first channel, like Hermes, not WhatsApp.
- **Asked:** would iMessage and WhatsApp be too open and dangerous, or fine if we code it right?
- **Answer:** the line is whose identity the channel is. A channel that is the bot's own account (a Telegram bot, a separate
  WhatsApp Business number, a separate Apple ID) is safe to build right. A bridge into your personal WhatsApp or iMessage is
  dangerous whatever the code: the bot can read every chat and send as you, every stranger's message becomes input that can
  carry instructions, and iMessage holds the text-message login codes for your accounts. Unofficial WhatsApp bridges also
  break WhatsApp's terms and can get your number banned.
- **Recorded:** Identity and reach area set to drafted with five decisions and a six-row channel comparison; new security
  rule (never bridge personal messaging accounts) and a new runtime threat (a personal messaging bridge).
- **Telegram caveats:** allow only your user ID, never join groups, bot token in the secrets broker, forwarded content is
  untrusted, and chats are not end-to-end encrypted (open question: keep sensitive topics in our own app).

## 2026-11-21 10:59 CT

- **Asked:** is Signal the best and easiest of all?
- **Answer:** the most private, not the easiest. Signal chats are end-to-end encrypted, so Signal's servers cannot read them
  (Telegram's can). But Signal has no official bot API: signal-cli is unofficial (GPL, run as a separate process), needs its
  own phone number and a captcha at sign-up, has no buttons for approval cards, and needs frequent updates because Signal
  stops serving old clients. Telegram takes minutes through BotFather and has buttons, which our approvals need.
- **Decided (Claude, overrule if wrong):** Telegram stays first; Signal becomes the second channel for sensitive topics once
  Telegram works. Open question changed to which topics must avoid Telegram.

## 2026-11-21 10:59 CT

- **Rule (operator):** once we decide, the area is edited down to the decision so it is not confusing; the reasoning lives here.
- **Applied to Identity and reach:** channel table now holds only Telegram (first), Signal (second) and our own app (later);
  the WhatsApp-bridge, iMessage-bridge, WhatsApp Business and separate-Apple-ID rows were removed (reasons in the entries above);
  repos that only served those channels (Baileys, wacli, imsg, BlueBubbles) left the area. One decided line keeps "not now:
  WhatsApp, iMessage" so the question does not come back.

## 2026-11-21 11:02 CT

- **Asked:** can Telegram be made end-to-end encrypted so its servers cannot read it? Is that how it is designed?
- **Answer:** yes, by design. Normal Telegram chats, bot chats included, are encrypted between your phone and Telegram, and
  Telegram holds the keys so chats sync across devices. End-to-end Secret Chats exist only between two people's phones, and
  bots cannot join them. No setting fixes that; encrypting messages ourselves would mean writing our own Telegram client.
- **The fix is design, not encryption:** Telegram becomes the doorbell (idea #78). Messages say only what is waiting; tapping
  opens a Telegram Mini App served from our own server over Tailscale, where details, files and approvals live and never
  touch Telegram's servers. To confirm at build time: the Mini App loads from a Tailscale HTTPS address on the phone.
- **Decided (operator):** Signal dropped as too hard; Telegram is the only chat channel. Area pruned: Signal row, decision and
  signal-cli repo removed; Signal moved to the "not now" line.

## 2026-11-21 11:04 CT

- **Operator:** Tailscale is running on my phone.
- **Recorded:** the Mini App prerequisite is met; the decision now says the Mini App stays on the tailnet with nothing public.
  Left to confirm at build time: HTTPS certificates turned on for the tailnet, BotFather accepting the ts.net address, and
  Telegram's in-app browser reaching it through Tailscale. Side effect to expect: details open only while Tailscale is connected.

## 2026-11-21 11:05 CT

- **Asked:** is the Telegram design overengineering?
- **Answer:** the Mini App part, yes, for now. It means a second web interface, sign-in checks inside Telegram, tailnet HTTPS
  certificates and more to secure, before the trial has shown the bots get used at all. The content rule costs nothing and
  covers the real risk. You ran Hermes on Telegram for months, so the channel itself is proven for you.
- **Decided (Claude, overrule if wrong):** version 1 is a plain Telegram bot with approval buttons and the content rule (no
  client names, money, health or credentials in messages; the bot says "open it on the Mac"). The Mini App (#78) waits until
  the trial shows sensitive approvals from the phone. Build-time Mini App checks removed from open questions.
- **During the MausBot trial:** use MausBot's own phone app over Tailscale for anything sensitive; that is the free test of
  whether a private phone view is needed at all.

## 2026-11-21 11:07 CT

- **Asked:** MausBot has an iOS app?
- **Answer:** yes, a native app on the App Store and Google Play. It pairs by QR code with the desktop app or with MausBot
  Cloud. For a self-hosted server like our test server there are two ways: the hosted MausBot Relay (end-to-end encrypted, but it
  needs a MausBot account and a third-party service) or the web app added to the Home Screen from a Tailscale HTTPS address.
  Its own docs say alerts arrive only while the app is connected (about 25 seconds after backgrounding on iPhone).
- **Decided (Claude, overrule if wrong):** the trial uses the web app over Tailscale, matching the Tailscale-only rule
  (plan.md phase 1, step 5). Weak phone push is one more reason Telegram stays the doorbell.

## 2026-11-21 11:08 CT

- **Asked:** why are we talking about Telegram if MausBot has an app? Is it another way to talk to the agent?
- **Answer:** two different things got mixed. In the MausBot trial we use MausBot's own app (web app over Tailscale) and
  Telegram plays no part. Telegram is for our own build later: our bots will have no phone app of their own, and a Telegram
  bot gives us one for free (chat, push notifications that actually arrive, approval buttons), the way Hermes did. Our own
  iOS app is the long-term option once the bots prove themselves.
- **Recorded:** the Identity and reach area now says up top that it is for our own build, with the reason for Telegram.

## 2026-11-21 11:12 CT

- **Asked:** clean up anything extra in the artifact and make sure all the data is correct.
- **Fixed:** idea #23 rewritten from "reach it from any chat app" (listed WhatsApp, Signal, iMessage) to Telegram only, matching
  the decision; idea #22 lost its chat-only wording and now states MausBot's meeting support exactly (Meet, Teams and Jitsi; Zoom
  links answered "not supported yet", checked in its docs); idea #51 source corrected to original.
- **Checked:** MausBot has no Telegram channel (only a "Telegram-style" look in its README), so #23 stays "MausBot lacks it".
  OWASP agentic category names confirmed by several secondary sources and corrected to ASI02 "tool misuse and exploitation",
  ASI04 "agentic supply chain vulnerabilities", ASI05 "unexpected code execution", ASI06 "memory and context poisoning" (now
  cited on idea #75); the OWASP link points at the 2026 list. Every design-area and threat link to an idea resolves (build check).
- **Not re-checked:** CVE version ranges (the page already says to confirm on NVD or GitHub advisories before citing them).

## 2026-11-21 11:19 CT

- **Asked:** what would the UI look like? Make a mockup and open it in Chrome. Also, there was a GitHub repo that looks like
  Slack but for humans and agents.
- **Found:** Buzz (block/buzz, Apache 2.0, 37,646 stars), released by Jack Dorsey's Block in July 2026: a self-hosted workspace
  where people and agents share channels, threads, DMs and canvases. Agents have their own keys and audit trail; every message
  and approval is a signed event (Nostr). Its README, 2026-11-21: works today: channels, threads, canvases, search, audit log,
  desktop app; being wired up: iOS and Android apps, approval gates; not built: push notifications. Smaller look-alikes:
  open-tag (218 stars), Zooid (68).
- **Built:** clickable mockup v1, mockups/bot-workspace-v1.html, opened in Chrome. Slack-style: channels, bots with trust
  levels, Waiting on you queue with recommended answers, approval cards, usage meter, Pause all bots, and a right panel with
  the bot's computer, memory and audit log; a phone preview of the Telegram doorbell. Example data only.
- **Asked:** do we use our own interface or Buzz?
- **Recommendation (operator decides):** Buzz as the workspace, our effort into the bots. A chat app (channels, threads,
  search, desktop, phones, sign-in) is the biggest build and not what makes ours different; Buzz is Apache 2.0, so we can depend
  on it or fork it if Block drops it; its agent keys and signed log already match our security rules. Risks: developer preview,
  approval gates unfinished, no phone push yet (Telegram stays the doorbell). Decide after a one-week Buzz trial; own interface
  only if Buzz fails it. The mockup then becomes our checklist of what Buzz must support.

## 2026-11-21 11:29 CT

- **Asked:** make a decision: our own mockup or Buzz?
- **Decided (Claude, at the operator's request):** Buzz is the workspace; we build the bots, not a chat app. Gate: a one-week
  Buzz trial after the MausBot trial (runs on our server, bots join as members, approvals work); own interface from the mockup
  only if Buzz fails. Telegram stays the phone doorbell until Buzz has push notifications. The mockup becomes the checklist of
  what the workspace must do.
- **Area pruned:** Bots and chat app is now decided; the own-or-Buzz and web-or-desktop questions are gone; repos cut to Buzz,
  the Buzz desktop app, and two fallbacks for our own interface (LibreChat, assistant-ui). open-tag, Zooid, Open WebUI,
  LobeHub and the Vercel chatbot left the area (reasons above in this log).

## 2026-11-21 11:33 CT

- **Operator:** I might not try it fully myself; build it, talk about it and share it with my community. Do we include Buzz
  code in the repo so whoever installs it gets the full package?
- **Pushback recorded:** the goal changes from a tool for you to a project for others. The old risk was "you stop using it";
  the new one is "people install an agent with logins and a browser that you never ran" (the OpenClaw lesson: tens of thousands
  of exposed installs). Rule added: you run every release yourself, long enough to film the demo, before anyone else installs
  it; it ships labeled experimental with safe defaults on.
- **Decided (Claude):** do not copy Buzz's code into our repo. Our one Docker Compose install pulls Buzz's official relay image
  (ghcr.io/block/buzz, pinned to an exact release and digest; its own bundle defaults to 0.3.0) with Postgres, Redis and MinIO,
  plus our bots and Tailscale. Upgrades are deliberate. The Buzz desktop app comes from Block's releases. README credits Buzz
  with its Apache 2.0 license; a patched copy, if ever needed, keeps the license and notes the changes. Reason: Buzz is a Rust
  relay, a Flutter app and a separate desktop repo changing daily; a copy would be ours to maintain forever.
- **Recorded:** new Packaging and install area (decided, with 4 verified repos); Product scope set to drafted (built to share,
  open source from the start); Read this first and Path from here updated (MausBot becomes a short look, not a long trial).

## 2026-11-21 11:44 CT

- **Asked:** what gaps are in the workbook that we did not discuss (context layer, agent management, memory, anything), based on
  what has been published about agents, work and productivity?
- **Answer:** nine gaps, checked against Anthropic's context engineering and long-running harness posts, HumanLayer's 12-Factor
  Agents, Cognition's multi-agent essays (2025 and 2026), the OpenTelemetry GenAI agent conventions, A2A v1.0 (Linux Foundation,
  March 2026), and three studies on real value (METR 2025: experienced developers 19% slower with AI while believing they were
  20% faster; MIT NANDA 2025: 95% of companies saw no profit impact from GenAI pilots; HBR and BetterUp "workslop": 40% of 1,150
  workers received AI work that pushed effort onto them).
- **Added:** a Gap analysis section and eight new design areas, all exploring, each with proposals marked "not decided", open
  questions and 5 reference repos rechecked with the GitHub API: Context layer, Long-running work, Bot management,
  Observability, Measuring real value, Interop and standards, Data and backups, Community release (21 areas in all).
- **Rules added to existing areas:** Bots working together: many bots may think, one bot writes (Cognition). Testing and
  quality: nothing a bot makes reaches another person until a reviewer step checks it (workslop; Anthropic's planner, maker,
  reviewer pattern).
- **Confirmed strength:** MIT NANDA's main reason AI tools fail is that they do not keep feedback or improve; our improving
  skills and memory aim straight at that.

## 2026-11-21 12:42 CT

- **Operator:** why worry about the server now; stop asking until we are ready to build. What is the build plan; do we create a
  PRD and a build plan with phases and tasks?
- **Done:** server and MausBot-trial questions deferred to build phase 1 (env #752, #782, #783) and no longer raised.
- **Finding that shaped the plan:** Buzz already ships buzz-acp, which runs any ACP agent as a Buzz member (answering only its
  owner by default), and claude-agent-acp runs Claude Code as an ACP agent. So we build neither a chat app nor an agent loop;
  our code is the layer that makes bots safe, useful and measurable: bot definitions, gatekeeper, memory server, doorbell,
  value log and installer.
- **Written (draft for approval):** PRD (problem, users, 5 goals, non-goals, architecture of 10 parts, 18 requirements,
  success measures, risks, open questions) and a build plan of 8 phases and 38 tasks, each with a done-when check and the
  requirements it serves. Phase 0 is five spikes that could change the design, including what buzz-acp does with Claude
  Code's permission requests. Sources: build/prd.json and build/plan.json, rendered on the page and as markdown.

## 2026-11-22 09:51 CT

- **Account:** the workbook moved to a new link under the account now signed in (env #813); both accounts need it shared from
  the Share menu (env #814).
- **Asked:** understand browser-use.com Web Agents and how to replicate it for our use without paying them.
- **Answer:** Web Agents is the hosted version: their model (BU 4.0, $1.80 and $9.00 per million tokens) drives their cloud
  browser ($0.06 per hour, proxies $5 per GB). Under it is the open-source library (MIT, 121,746 stars): the model writes Python
  in one persistent session that drives Chrome over the DevTools Protocol, then a judge pass checks the run. What only the
  paid cloud adds: a stealth Chromium, residential proxies, automatic CAPTCHA solving, cloud profiles and recordings.
- **Proposed for our build:** Browser Harness (MIT, 19,192 stars) lets Claude Code drive Chrome directly, so browser work runs
  on the Claude plan with no Browser Use account and no per-token API bill. Run it in each bot's desktop container with a
  persistent profile; keep Cua for non-browser apps; telemetry off; never share a live-view link. We do not ship stealth,
  proxy rotation or CAPTCHA bypass: a blocked bot stops and asks. New build task P0.6 compares Browser Harness with Cua.

## 2026-11-22 09:56 CT

- **Asked:** if we pay Browser Use, how do they get around it? Are they not breaking the terms of service by selling this?
- **Correction (Claude):** the earlier wording overstated it. Terms of service are a contract between a site and the person
  using it, so the tool seller is usually not the one breaking them; sellers put that responsibility on customers in their own
  terms. Paying them does not make a use allowed; it moves the tooling, not the responsibility. Whether a use is allowed depends
  on the site and the data: Meta v. Bright Data (2024) found logged-out scraping of public pages did not breach Meta's terms,
  while a logged-in account is bound by terms you accepted. Many sites allow automation; some forbid it. Not legal advice.
- **Revised proposal:** off by default with no stealth or CAPTCHA bypass (a blocked bot stops and asks), and a per-bot opt-in to
  a paid stealth cloud browser for users who choose it, with the docs stating the responsibility plainly. The real reason for
  the default is that a community project should not make that choice for every installer.

## 2026-11-22 10:04 CT

- **Asked:** think up about 20 different names for the product.
- **Answer:** 20 candidates across four themes (crew and duty roster, steadiness, flocks and hives, helpers), each checked for
  the most-starred GitHub repo using the name. Dropped before listing because an agent project already uses them: Understudy
  (understudy-ai, 467 stars) and Quarterdeck ("build always-on agents", 45 stars); also dropped for big existing projects:
  Lantern, Shipyard, Hearth. Recommended: Muster, Watchbill, Mainstay. GitHub only; trademark, domain and package names are
  checked once there is a shortlist. Avoided: names tied to an earlier rejected idea and anything close to Buzz, Grok, Claw or Muse.

## 2026-11-22 10:10 CT

- **Operator:** I want a name that is not used; why offer names other projects use?
- **Correction (Claude):** the first list was real words, and every real word is taken somewhere. Withdrawn.
- **Done:** 50 invented names run through naming/namecheck.sh (exact GitHub repo name, npm, PyPI, .com and .dev domains;
  the domain checker passed a known-answer control). 28 passed GitHub, npm, PyPI and .dev; 20 offered. Four are free as .com
  too and have no web results: Crewveil, Bosunry, Hivemere, Shiftmere. Most invented .com names are already registered by
  domain resellers (Mustrel.com was registered 2026-08-11). Trademark check comes after the pick.

## 2026-11-22 10:21 CT

- **Operator:** Helmgard sounds cool, like a Game of Thrones or fantasy place. It could be a .dev domain if we go that way.
- **Checked:** helmgard.dev is free; helmgard.com is parked for sale (registered 2008); .io, .ai, .co, .net and .org look free.
  The web only shows Helmgard Keep, a place in the video game Kingdoms of Amalur, which fits the fantasy feel and is not a brand.
- **Flag (Claude):** a pending US trademark application for HELMGUARD (serial 99077620, filed 2025-03-11, classes 9, 42 and
  45, covering software and tech services). One letter off and sounds the same, in our category. A .dev domain does not solve a
  trademark conflict. Not legal advice. Options: accept the risk for a free community project, ask a trademark attorney, or pick
  a close alternative with no hits (Wardmere, Mustergate). Not renamed yet; no domain bought.

## 2026-11-22 10:24 CT

- **Operator:** Helmgate?
- **Checked:** fails. A Go project on GitHub was called helmgate (autom8ter/helmgate, a Kubernetes deploy API, since renamed
  kdeploy), a PyPI package named helmgate exists, and helmgate.com has been registered since 2001. "Helm" in software also
  points straight at Helm, the Kubernetes package manager, so the name would read as Kubernetes tooling. No US trademark found.
  helmgate.dev is free, but the other conflicts rule it out.

## 2026-11-22 10:31 CT

- **Operator:** yes, more fantasy-place names like Helmgard; nothing nautical.
- **Done:** 40 new names checked with naming/namecheck.sh (results in naming/2026-11-22-fantasy-batch.txt): 32 passed GitHub,
  npm, PyPI and .dev, 22 of them free as .com too. Web search on eight: clean with no results and .com free: Ironwyck, Embrigard, Ardengard, Brynhold, Skaldhold.
  Thalgard is a castle in the game Enderal, Halvgard an old Norwegian farm-tax word, Corrigard close to a packaging brand
  (Corruguard). Recommended: Ironwyck. Trademark search on the final pick.

## 2026-11-22 10:38 CT

- **Decided (operator):** the product is called **Ardengard**.
- **Checked before adopting:** no GitHub repo, npm, PyPI, crates.io or Docker Hub package by that name; ardengard.com and
  ardengard.dev free; .io, .ai, .co, .net and .org look free; no web results. github.com/ArdenGard is a personal account (one
  Portuguese text-RPG repo, 0 followers), so our organization will be ardengard-dev or ardengardhq (both free). Trademark: no
  ARDENGARD record found; a pending ARDEN application (Arden Technologies, 99529300, software classes 9 and 42) shares the
  first part, lower risk than HELMGUARD, still to confirm with an official USPTO search before release. Not legal advice.
- **Renamed:** PRD and build plan say Ardengard; build task P1.1 now creates the ardengard repo under the new organization
  and registers ardengard.dev. The project folder keeps its mausbot-experiment path until the repo exists.

## 2026-11-22 10:44 CT

- **Asked:** create a repo for Ardengard and set up a local repo, moving all the files and research into proper folders.
- **Done:** local repo in the FerryMail layout: docs/product (PRD), docs/plan (build plan,
  MausBot look plan), docs/design/mockups, dated docs/research folders with an index, workbook/ (source and generated
  markdown), scripts/ (build_workbook.py, namecheck.sh), tests/ (3 build tests, passing), artifacts/agent-wishlist/ with a
  versions log, AGENTS.md, CLAUDE.md, README, backlog and lessons file. The scratchpad folder holds only a pointer now.
- **Waiting on the operator:** where the GitHub repo lives (which account or a new organization) and whether it is public
  or private. Nothing is pushed until then.

## 2026-11-22 10:56 CT

- **Decided (operator):** the GitHub repo is public now, under the operator's personal GitHub account.
- **Operator:** personal details can go in separate folders that are git-ignored.
- **Done:** a git-ignored private/ folder and CLAUDE.local.md now hold the account names, server details, earlier projects,
  business specifics and the unabridged log. Public files use generic wording; the earlier entries in this log were edited for
  privacy only, and the full originals are kept privately. The unpublished first commit was rewritten so the history holds
  none of the private details.

## 2026-11-22 11:19 CT

- **Asked:** create a mascot and icon in Codex; five ideas on a contact sheet in the browser.
- **Done:** five icon and mascot pairs generated with Codex image generation into brand/concepts/2026-11-22-codex/ (prompt,
  run log, 10 images at 1024 px) and a contact sheet opened in Chrome. Palette: forest green, ember gold, parchment, slate.
  Concepts: Forest Keep with Owl Warden, Oak Shield with Fox Knight, Lit Gate with Stone Keeper, Raven Tower with Raven Scribe,
  Key Leaf with Badger Keyholder.
- **Claude's read:** Key Leaf is the strongest icon (one bold shape that still reads at 32 px, and keys mean permissions).
  Forest Keep reads more like a hut than a keep. Owl Warden and Raven Scribe are the strongest mascots; the raven ties to
  memory (Odin's ravens are Thought and Memory). Icons and mascots can be mixed across concepts.

## 2026-11-22 11:32 CT

- **Asked:** are these suitable for a Grok Bot style agent team?
- **Answer:** partly. Grok Bot, Muse, dots and Cue use modern minimal marks, so the storybook icons look like a cozy game next
  to them, and one mascot says "one assistant" when the product is a team. But builder communities love mascots, and the five
  characters already map to the bot roles. Recommendation: Key Leaf as the icon, all five mascots as the default crew.
- **Decided (operator):** reimagine it in that concept.
- **Done:** round 2 in brand/concepts/2026-11-22-codex-round-2/: five circular crew avatars simplified for chat size (Owl
  Warden as Chief of Staff, Raven Scribe as Researcher, Fox as Writer, Badger Keyholder as Gatekeeper, Stone Keeper as Ops
  Watch), a crew lineup at the gate for the README, and three modern Key Leaf icons (geometric, negative space, monoline)
  compared with the round 1 original at 64 and 32 px on light and dark. Contact sheet opened in Chrome.
- **Claude's read:** icon A (geometric key) is the strongest: modern, bold, reads at 32 px. Icon C's thin line fades at small
  sizes; icon B's tile inside a tile looks boxed in. The lineup is ready as the README hero image.

## 2026-11-22 11:35 CT

- **Asked:** other roles we could create mascots for, and what else to provide out of the box for someone installing it.
- **Answer:** ten more roles for an extended cast (Hare, Inbox Steward; Rooster, Morning Brief; Squirrel, Memory Keeper; Heron,
  Reviewer; Hawk, Watcher; Mole, Builder; Porcupine, Security Tester; Mouse, Bookkeeper; Robin, Messenger; Stag, Guide),
  avoiding animals other products already own (hedgehog, beaver, tortoise, firefly, otter, bee, lobster). New design area
  Out of the box: the core five ship by default; proposed demo mode with fake data, five day-one starter jobs, bot folders with
  tested skills and safe permissions, a getting-to-know-you interview for the core profile, a routines library, crew packs by
  kind of user, an ardengard doctor command, a plain-language permissions page, rename and recolor. Four reference repos
  verified with gh (crewAI-examples dropped: archived).

## 2026-11-22 11:37 CT

- **Operator:** each one will have a role defined for its purpose.
- **Done:** crew catalog docs/product/crew.json (draft for approval), shown in a new The crew section and generated as
  crew.md. Five rules (one role per bot; the never list is enforced by the gatekeeper; only the operator widens permissions;
  one writer per task; rename and recolor allowed), four permission levels (read, draft, ask, never), and fifteen role cards
  with purpose, does, never, default permissions, starter skills, routines and who each works with. Core crew of six: Owl
  Warden, Raven Scribe, Fox, Heron (Reviewer, added to the core because the review step is required), Badger Keyholder, Stone
  Keeper. Extended cast of nine. Packs: Solo founder, Small business, Developer, Researcher or student, Content creator, First run.
- **Operator:** does not like icons A, B or C; the leaf-shaped key head looks like a vulva, especially B.
- **Correction (Claude):** agreed; a pointed oval split by a center line reads that way, and Claude recommended A without
  seeing it. A, B and C are dropped; icon round 3 avoids that shape and every concept is checked for unintended readings first.

## 2026-11-22 11:43 CT

- **Asked:** are the new mascots repeats of the present ones?
- **Answer:** some duties were. Robin (posts and replies) duplicated the Writer, Rooster's morning brief duplicated the Chief
  of Staff's morning plan, Hare drafted replies the Writer owns, and Hawk's name "Watcher" clashed with Ops Watch. Fixed in
  docs/product/crew.json: Robin removed, Rooster is Scheduler only, Hare triages and hands replies to the Writer, Hawk renamed
  Scout (watches the outside world; the Stone Keeper watches our own system). 14 roles, each with one job no other role does.
  Five of the cast are birds (owl, raven, heron, rooster, hawk), so their avatars must stay visually distinct.
- **Icon round 3 (after A, B and C were rejected):** six concepts with strict shape rules, checked at full size and at 64 and
  32 px for unintended readings before showing; none found. Claude's read: Gatehouse is the strongest and safest. Owl Mark is
  the most distinctive and ties to the crew, but a green owl face strongly recalls Duolingo's owl (Hootsuite also uses an owl).
  Round Key is clear but is the stock password-manager key. Lit Arch reads as a sunrise, Crew Crown as a loading indicator,
  Shield Window as a bowl or boat.

## 2026-11-22 11:44 CT

- **Operator:** update the same contact sheet; no need to create a new file.
- **Done:** one living sheet, brand/contact-sheet.html, holds every round newest first with status chips (round 3 icons,
  the crew, round 2 icons rejected, round 1). The three per-round sheets were removed. Saved as a standing rule.
- **Operator:** the Gatehouse icon is the closest to nice in this group.
- **Next:** a refinement round of Gatehouse variants, added to the same sheet.

## 2026-11-22 11:49 CT

- **Operator:** rename the sheet Ardengard brand sheet, keep updating it, remove past rounds and keep the latest.
- **Done:** brand/ardengard-brand-sheet.html shows only the current state: the latest icon round and the crew; no past rounds,
  no status labels. Past rounds stay in brand/concepts/ dated folders. Standing rule updated.
- **Gatehouse refinements (round 4):** bolder, forest, night, gold, crew lights, badge, checked at full and small sizes; no
  unintended readings. Claude's pick: Forest (pines behind the gatehouse: forest and keep, the name in one image). The Night
  version's moon came out lumpy.

## 2026-11-22 13:52 CT

- **Operator:** save and document everything so the session can be closed.
- **State at close:** design phase. Waiting on the operator: approve the PRD and build plan (backlog #3), share the workbook
  page with the second Claude account (#4), pick the Gatehouse icon (#17; Claude recommends Forest) and confirm the crew (#16).
  Next build step once approved: phase P0, the six spikes. Brand work shipped to GitHub in this close-out.
