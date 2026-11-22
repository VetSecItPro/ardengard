# Ardengard

An open-source, self-hosted team of AI bots that work for you: Claude Code bots that live in a
[Buzz](https://github.com/block/buzz) workspace, each with its own sandboxed computer, that learn through skill files,
remember through plain-file memory, and ask before every risky action.

**Status: design.** The product requirements and build plan are drafts waiting for approval. No product code yet.

## Where things are

| Read | File |
|---|---|
| The whole design, easy to browse | [Agent Wishlist page](https://claude.ai/artifact/6z3iQwNWjHH9zJghwSj9s9) (private) |
| Product requirements | [`docs/product/prd.md`](docs/product/prd.md) |
| Build plan (8 phases) | [`docs/plan/plan.md`](docs/plan/plan.md) |
| Design areas, ideas, security and memory design | [`workbook/wishlist.md`](workbook/wishlist.md) |
| How every decision was made | [`docs/discussion-log.md`](docs/discussion-log.md) |
| Research | [`docs/research/`](docs/research/README.md) |
| UI mockup | [`docs/design/mockups/bot-workspace-v1.html`](docs/design/mockups/bot-workspace-v1.html) |

## The idea in one paragraph

Grok Bot, Muse, dots and Cue sell AI coworkers with their own computers, but they are closed and hold your data. The
open-source alternatives rebuild their own chat apps and shipped serious security holes in 2026. Ardengard builds
neither a chat app nor an agent loop: Buzz is the workspace, Buzz's `buzz-acp` connector runs Claude Code as a member,
and Ardengard is the layer that makes the bots safe, useful and measurable: bot definitions, a gatekeeper for every
action, a memory server, a Telegram doorbell, a value log and a one-command installer.

## Develop

```
python3 scripts/build_workbook.py
python3 -m unittest discover -s tests -v
```
