#!/usr/bin/env python3
"""Repository-specific integrity checks; not a behavioral Skill evaluation."""
from __future__ import annotations
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CORE = ("AGENTS.md", "BUILD_STATE.md", "GOAL_AND_USE_CASES.md", "PLUGIN_CONTRACT.md", "SHARED_TOOL_CAPABILITIES.md")
ERRORS = []
LINK = re.compile(r"(?<!!)\]\(([^)\n]+)\)")
GOALS = re.compile(r"(?m)^#### G(\d{3}):")
CASES = re.compile(r"(?m)^- UC(\d{3}):")
ROUTES = re.compile(r"^\|\s*G(\d{3})[–-]G(\d{3})\s*/\s*UC(\d{3})[–-]UC(\d{3})\s*\|", re.M)

def error(message):
    ERRORS.append(message)
    print("ERROR: " + message, file=sys.stderr)

def links(file):
    for hit in LINK.finditer(file.read_text(encoding="utf-8")):
        raw = hit.group(1).strip().split(" ", 1)[0].strip("<>")
        if raw.startswith(("#", "/", "http://", "https://", "mailto:", "data:")):
            continue
        name = unquote(raw.split("#", 1)[0].split("?", 1)[0])
        if not name:
            continue
        target = (file.parent / name).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            error(f"{file.relative_to(ROOT)}: missing/out-of-tree link {raw}")

def contiguous(items, label):
    if not items or items != list(range(1, len(items) + 1)):
        error(f"{label} IDs must be unique, ordered and contiguous: found {len(items)}")

def main():
    for name in CORE:
        f = ROOT / name
        if not f.is_file() or not f.read_text(encoding="utf-8").strip():
            error(f"Missing or empty mandatory document: {name}")
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        error("At least one Skill is required")
    for entry in skills:
        if not (entry.parent / "references").is_dir():
            error(f"Missing references directory: {entry.parent.relative_to(ROOT)}")
    markdown = [ROOT / p for p in CORE if (ROOT / p).exists()]
    markdown += list((ROOT / "skills").rglob("*.md"))
    markdown += list((ROOT / "docs").rglob("*.md"))
    for f in markdown:
        if not f.read_text(encoding="utf-8").strip():
            error(f"Empty Markdown: {f.relative_to(ROOT)}")
        links(f)
    goal_file = ROOT / "GOAL_AND_USE_CASES.md"
    handoff = ROOT / "docs/domain-handoffs/ci-cd-quality-engineering.md"
    if goal_file.exists() and handoff.exists():
        goal_text = goal_file.read_text(encoding="utf-8")
        goals = [int(v) for v in GOALS.findall(goal_text)]
        cases = [int(v) for v in CASES.findall(goal_text)]
        contiguous(goals, "Goal")
        contiguous(cases, "Use-case")
        rows = ROUTES.findall(handoff.read_text(encoding="utf-8"))
        if not rows:
            error("Handoff lacks goal/use-case coverage routes")
        covered_goals, covered_cases = set(), set()
        for ga, gb, ca, cb in rows:
            a, b, c, d = map(int, (ga, gb, ca, cb))
            if a > b or c > d:
                error(f"Inverted route G{ga}-G{gb} / UC{ca}-UC{cb}")
                continue
            g, u = set(range(a, b+1)), set(range(c, d+1))
            if (g & covered_goals) or (u & covered_cases):
                error(f"Overlapping route G{ga}-G{gb} / UC{ca}-UC{cb}")
            covered_goals.update(g)
            covered_cases.update(u)
        if covered_goals != set(goals) or covered_cases != set(cases):
            error(f"Coverage incomplete: {len(covered_goals)}/{len(goals)} goals; {len(covered_cases)}/{len(cases)} UCs")
        print(f"Traceability: {len(rows)} routes, {len(covered_goals)} goals, {len(covered_cases)} cases (authoring only)")
    else:
        error("Canonical goals or Domain-1 handoff is missing")
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} integrity issue(s)", file=sys.stderr)
        return 1
    print(f"PASS: {len(skills)} skill(s), {len(markdown)} Markdown files linked; no behavioral validation claimed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
