# Ardengard Backlog

Rules: `~/.claude/standards/BACKLOG_STANDARD.md`. Status words: OPEN, IN PROGRESS, WAITING ON OPERATOR, BLOCKED,
DONE, DROPPED. Central time on every stamp. Planned work lives in `docs/plan/plan.json`, one row per phase here
(#6 to #13); this backlog also holds setup, decisions and operator actions. Work before this repo existed:
`17.scratchpad` env #780 to #819.

## Open

| # | Task | Status |
| --- | --- | --- |
| 3 | Approve the PRD and build plan (docs/product/prd.json, docs/plan/plan.json) or say what to change | WAITING ON OPERATOR 2026-11-22 10:43 CT |
| 4 | Share the Agent Wishlist page with the operator's second Claude account (Share menu, edit access) | WAITING ON OPERATOR 2026-11-22 10:43 CT |
| 5 | Official USPTO search for ARDENGARD and close marks (pending ARDEN, serial 99529300, classes 9 and 42) before release 1 | OPEN 2026-11-22 10:43 CT |
| 6 | Plan phase P0: Spikes, prove the unknowns; 6 tasks | OPEN 2026-11-22 10:43 CT |
| 7 | Plan phase P1: Foundation; 5 tasks | OPEN 2026-11-22 10:43 CT |
| 8 | Plan phase P2: First bot; 5 tasks | OPEN 2026-11-22 10:43 CT |
| 9 | Plan phase P3: Gatekeeper and doorbell; 5 tasks | OPEN 2026-11-22 10:43 CT |
| 10 | Plan phase P4: Memory and context; 5 tasks | OPEN 2026-11-22 10:43 CT |
| 11 | Plan phase P5: Computer and long jobs; 4 tasks | OPEN 2026-11-22 10:43 CT |
| 12 | Plan phase P6: Observe and harden; 4 tasks | OPEN 2026-11-22 10:43 CT |
| 13 | Plan phase P7: Release to the community; 5 tasks | OPEN 2026-11-22 10:43 CT |
| 15 | Brand round 1: five mascot and icon concepts made with Codex image generation, shown on a contact sheet in the browser (operator) | WAITING ON OPERATOR 2026-11-22 11:19 CT: concepts in brand/concepts/2026-11-22-codex/; pick an icon and a mascot (can mix across concepts) |
| 16 | Brand round 2: the mascots as the bot crew (avatars, lineup) and modern Key Leaf icon variants (operator) | WAITING ON OPERATOR 2026-11-22 11:32 CT: 9 images and contact sheet in brand/concepts/2026-11-22-codex-round-2/; operator picks the icon (Claude recommends A) and confirms the crew |
| 17 | App icon: round 3 after the leaf-key icons were rejected; Gatehouse leads (operator), refinement round next | IN PROGRESS 2026-11-22 11:44 CT |

## Done

| # | Task | Status |
| --- | --- | --- |
| 2 | GitHub home: VetSecItPro/ardengard, public (operator) | DONE 2026-11-22 11:08 CT: repo created; operator pushed main (abb28e7); PR #1 added the CI docs gate, green, squash-merged as 73ee2b7; delete_branch_on_merge on |
| 14 | First PR: CI workflow that runs the build check and unit tests on every pull request | DONE 2026-11-22 10:58 CT: .github/workflows/ci.yml (docs-gate: build, generated files current, unit tests; GitHub-hosted runner, public repo) |
| 1 | Create the repo locally and move every design file from 17.scratchpad/mausbot-experiment into this layout | DONE 2026-11-22 10:43 CT: 38.ardengard created; docs/product, docs/plan, docs/design, dated docs/research, workbook, scripts, tests, artifacts/agent-wishlist; first local commit |
