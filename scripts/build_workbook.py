#!/usr/bin/env python3
"""Build the Agent Wishlist page and the generated markdown from the workbook sources.

Sources: workbook/ideas.json, workbook/template.html, docs/discussion-log.md,
docs/product/prd.json, docs/plan/plan.json.
Outputs: artifacts/agent-wishlist/index.html (the published page), workbook/wishlist.md,
docs/product/prd.md, docs/plan/plan.md.
Run from the repo root: python3 scripts/build_workbook.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
TIER = {"parity": "Match Grok Bot", "beyond": "Go past it", "moonshot": "Moonshot"}
MB = {"has": "has it", "partial": "partly", "missing": "lacks it"}
EFF = {"S": "small", "M": "medium", "L": "large"}
BANNED = ("—", "–")


def parse_log(path: pathlib.Path) -> list:
    """Turn discussion-log.md into [{when, items}]: one entry per '## ' heading, one item per top-level bullet."""
    entries, cur, item = [], None, None
    for raw in path.read_text().splitlines():
        if raw.startswith("## "):
            cur = {"when": raw[3:].strip(), "items": []}
            entries.append(cur)
            item = None
        elif cur is None:
            continue
        elif raw.startswith("- "):
            item = raw[2:].strip()
            cur["items"].append(item)
        elif raw.startswith("  ") and raw.strip() and cur["items"]:
            cur["items"][-1] += " " + raw.strip()
    for e in entries:
        e["items"] = [i.replace("**", "").replace("`", "") for i in e["items"]]
    return entries


def write_build_md(bdir: pathlib.Path, prd: dict, plan: dict) -> None:
    """Generate prd.md and plan.md from their JSON sources."""
    p = [f"# {prd['title']}", "", f"Status: {prd['status']}. Updated {prd['updated']}. Generated from prd.json; do not edit by hand.", "",
         f"Working name: {prd['working_name']}", "", "## Problem", ""] + [f"- {x}" for x in prd["problem"]]
    p += ["", "## Users", ""] + [f"- **{u['who']}:** {u['need']}" for u in prd["users"]]
    p += ["", "## Goals", ""] + [f"- {x}" for x in prd["goals"]]
    p += ["", "## Not in version 1", ""] + [f"- {x}" for x in prd["non_goals"]]
    p += ["", "## Architecture", "", prd["architecture"]["summary"], "", "| Part | Role | Source | Ours |", "|---|---|---|---|"]
    p += [f"| {x['part']} | {x['role']} | {x['source']} | {'yes' if x['ours'] else 'no'} |" for x in prd["architecture"]["parts"]]
    p += ["", "## Requirements", "", "| ID | Area | Requirement |", "|---|---|---|"] + [f"| {r['id']} | {r['area']} | {r['text']} |" for r in prd["requirements"]]
    p += ["", "## Non-functional", ""] + [f"- {x}" for x in prd["nonfunctional"]]
    p += ["", "## Success measures", ""] + [f"- {x}" for x in prd["metrics"]]
    p += ["", "## Risks", "", "| Risk | Plan |", "|---|---|"] + [f"| {r['risk']} | {r['plan']} |" for r in prd["risks"]]
    p += ["", "## Open questions", ""] + [f"- {x}" for x in prd["open_questions"]] + [""]
    (ROOT / "docs" / "product" / "prd.md").write_text("\n".join(p))
    b = [f"# {plan['title']}", "", f"Status: {plan['status']}. Updated {plan['updated']}. Generated from plan.json; do not edit by hand.", "", "## Rules", ""]
    b += [f"- {x}" for x in plan["rules"]] + [""]
    for ph in plan["phases"]:
        b += [f"## {ph['id']} {ph['name']}", "", f"Goal: {ph['goal']}", "", f"Exit check: {ph['exit']}", "", "| Task | What | Done when | Requirements |", "|---|---|---|---|"]
        b += [f"| {t['id']} | {t['task']} | {t['done']} | {', '.join(t['req'])} |" for t in ph["tasks"]] + [""]
    (ROOT / "docs" / "plan" / "plan.md").write_text("\n".join(b))


def main() -> int:
    data = json.loads((ROOT / "workbook" / "ideas.json").read_text())
    ids = [i["id"] for i in data["ideas"]]
    if len(ids) != len(set(ids)):
        sys.exit("duplicate idea ids")
    keys = {t["key"] for t in data["themes"]}
    for i in data["ideas"]:
        if i["theme"] not in keys or i["tier"] not in TIER or i["mausbot"] not in MB or i["effort"] not in EFF:
            sys.exit(f"idea {i['id']} has an unknown theme, tier, status or effort")

    data["log"] = parse_log(ROOT / "docs" / "discussion-log.md")
    bdir = ROOT / "docs"
    data["prd"] = json.loads((bdir / "product" / "prd.json").read_text())
    data["plan"] = json.loads((bdir / "plan" / "plan.json").read_text())
    rids = {r["id"] for r in data["prd"]["requirements"]}
    akeys = {a["key"] for a in data.get("areas", [])}
    for r in data["prd"]["requirements"]:
        if r["area"] not in akeys:
            sys.exit(f"requirement {r['id']} points at unknown area {r['area']}")
    for ph in data["plan"]["phases"]:
        for tk in ph["tasks"]:
            for rq in tk["req"]:
                if rq not in rids:
                    sys.exit(f"task {tk['id']} points at unknown requirement {rq}")
    write_build_md(bdir, data["prd"], data["plan"])
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = (ROOT / "workbook" / "template.html").read_text().replace("__DATA__", payload)
    out_dir = ROOT / "artifacts" / "agent-wishlist"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "index.html").write_text(html)

    lines = [
        "# Agent Wishlist",
        "",
        f"Generated from `ideas.json` by `scripts/build_workbook.py`. Updated {data['updated']}. Do not edit by hand.",
        "",
        f"{len(data['ideas'])} ideas. MausBot column: has it, partly, or lacks it (as read 2026-11-21).",
        "",
    ]
    gaps = data.get("gaps")
    if gaps:
        lines += ["## Gap analysis", "", gaps["intro"], "", "| Gap | Why | Source | Fix |", "|---|---|---|---|"]
        lines += [f"| {g['gap']} | {g['why']} | {g['source']} | {g['fix']} |" for g in gaps["items"]]
        lines += ["", gaps["confirmed"], ""]
        akeys = {a["key"] for a in data.get("areas", [])}
        for g in gaps["items"]:
            if g["area"] not in akeys:
                sys.exit(f"gap '{g['gap']}' points at unknown area {g['area']}")
    lines += ["## Design areas", ""]
    for a in data.get("areas", []):
        lines += [f"### {a['name']} ({a['status']})", "", a["summary"], "", "Decided:"]
        lines += [f"- {x}" for x in a["decided"]] or ["- nothing yet"]
        if a.get("proposed"):
            lines += ["", "Proposed, not decided:"] + [f"- {x}" for x in a["proposed"]]
        lines += ["", "Open questions:"] + ([f"- {x}" for x in a["open"]] or ["- none"])
        lines += ["", "Ideas: " + ", ".join(f"#{n}" for n in a["ideas"])]
        for r in a.get("repos", []):
            lines.append(f"- Reference repo: {r['repo']} ({r['stars']} stars, {r['license']}): {r['study']}")
        lines.append("")
        for n in a["ideas"]:
            if n not in set(ids):
                sys.exit(f"area {a['key']} points at unknown idea #{n}")
    mem = data.get("memory")
    if mem:
        lines += ["## Memory detail", "", mem["stance"], "", "| Kind | Holds | Example | Kept in | From |", "|---|---|---|---|---|"]
        lines += [f"| {l['name']} | {l['holds']} | {l['example']} | {l['kept']} | {l['from']} |" for l in mem["layers"]]
        lines += ["", "Write pipeline:"] + [f"{k}. {s}" for k, s in enumerate(mem["pipeline"], 1)]
        lines += ["", "Build order:"] + [f"- {s}" for s in mem["stack"]]
        lines += ["", "| Repo | Stars | License | What | Take | Verdict |", "|---|---|---|---|---|---|"]
        lines += [f"| {r['repo']} | {r['stars']} | {r['license']} | {r['what']} | {r['take']} | {r['verdict']} |" for r in mem["repos"]]
        lines.append("")
    lines += ["## Idea catalog", ""]
    for t in data["themes"]:
        lines += [f"### {t['name']}", "", t["blurb"], "", "| # | Idea | Reach | MausBot | Build | From |", "|---|---|---|---|---|---|"]
        for i in data["ideas"]:
            if i["theme"] == t["key"]:
                lines.append(f"| {i['id']} | **{i['title']}**: {i['what']} For you: {i['why']} | {TIER[i['tier']]} | {MB[i['mausbot']]} | {EFF[i['effort']]} | {', '.join(i['from'])} |")
        lines.append("")
    sec = data.get("security")
    if sec:
        lines += ["## Security model", "", sec["stance"], "", "### Lessons from other projects' code", "", sec["code_intro"], "",
                  "| Lesson | Seen in | Our rule | OWASP |", "|---|---|---|---|"]
        for c in sec["code_lessons"]:
            lines.append(f"| {c['lesson']} | {c['seen']} | {c['rule']} | {c['owasp']} {sec['owasp'].get(c['owasp'], '')} |")
        lines += ["", "### Threats while the bots run", "", "| Threat | Example | Defense | Ideas |", "|---|---|---|---|"]
        for x in sec["threats"]:
            lines.append(f"| {x['threat']} | {x['example']} | {x['defense']} | {', '.join('#' + str(n) for n in x['ideas'])} |")
        lines += ["", "### Design rules for our repo", ""] + [f"- {r}" for r in sec["rules"]] + [""]
        known = set(ids)
        for x in sec["threats"]:
            for n in x["ideas"]:
                if n not in known:
                    sys.exit(f"threat '{x['threat']}' points at unknown idea #{n}")
    md = "\n".join(lines)
    (ROOT / "workbook" / "wishlist.md").write_text(md)

    for name, text in (("html", html), ("md", md)):
        if any(c in text for c in BANNED):
            sys.exit(f"{name} output contains an em or en dash")
    print(f"built {len(data['ideas'])} ideas: artifacts/agent-wishlist/index.html, workbook/wishlist.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
