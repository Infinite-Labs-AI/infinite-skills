#!/usr/bin/env python3
"""Validate the curated marketing skills without third-party dependencies."""

from __future__ import annotations

import re
import sys
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SOURCE_ROOT = Path(
    "/Users/chaosalchemist/.hermes/sandboxes/docker/default/workspace/"
    "infinite skills - organized/skills_by_function"
)

FORBIDDEN_KEYS = {
    "author",
    "platforms",
    "user-invocable",
    "argument-hint",
    "allowed-tools",
    "requires",
    "metadata",
    "version",
}

DENY_PHRASES = [
    "Check for product marketing context first",
    "You are an expert",
    "Top 3 Actions",
    "Health Score: X/100",
    "ranked by estimated $ impact",
    "Ready to install this series",
    "DESIGN_VARIANCE",
    "Double-Bezel",
    "anti-slop",
    "Clarity over cleverness",
    "Benefits over features",
    "Specificity over vagueness",
    "Critical rules",
    "Record findings",
    "For ongoing",
    "Connect your ESP via Cogny",
]

SOURCE_STYLE_HEADINGS = {
    "Usage",
    "Steps",
    "Before Starting",
    "Initial Assessment",
    "Related Skills",
    "Prerequisites Check",
    "Critical rules",
    "Output Format",
}

EXPECTED_MARKETING_SKILLS = {
    "ab-testing",
    "ai-seo",
    "analytics-tracking",
    "cold-outreach",
    "competitor-analysis",
    "content-strategy",
    "copywriting",
    "creative-brief",
    "cro-audit",
    "customer-research",
    "distribution-plan",
    "ecommerce-app-cro",
    "email-sequence",
    "launch-loop-strategy",
    "launch-strategy",
    "marketing-brief",
    "marketing-plan",
    "offer-design",
    "paid-ads",
    "partnerships",
    "positioning",
    "retention",
    "sales-enablement",
    "seo-strategy",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(f"{path} is missing YAML frontmatter")
    fields: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        if not raw.strip():
            continue
        if ":" not in raw:
            fail(f"{path} has malformed frontmatter line: {raw}")
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        fields[key] = value
    return fields


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def shingles(text: str, size: int = 8) -> set[tuple[str, ...]]:
    tokens = words(text)
    if len(tokens) < size:
        return set()
    return {tuple(tokens[i : i + size]) for i in range(len(tokens) - size + 1)}


def normalized_lines(text: str) -> set[str]:
    lines: set[str] = set()
    for raw in text.splitlines():
        line = re.sub(r"\s+", " ", raw.strip().lower())
        if len(line) >= 45 and not line.startswith(("---", "name:", "description:")):
            lines.add(line)
    return lines


def sections(text: str) -> list[str]:
    parts = re.split(r"^##+\s+.+$", text, flags=re.M)
    return [part.strip() for part in parts if len(words(part)) >= 30]


def source_names() -> set[str]:
    names: set[str] = set()
    if not SOURCE_ROOT.exists():
        if os.environ.get("ALLOW_MISSING_SOURCE_CORPUS") == "1":
            return names
        fail(f"source corpus not found: {SOURCE_ROOT}")
    source_files = list(SOURCE_ROOT.glob("*/*/SKILL.md"))
    if not source_files:
        fail(f"source corpus contains no SKILL.md files: {SOURCE_ROOT}")
    for skill in source_files:
        folder = skill.parent.name
        if "__" in folder:
            names.add(folder.split("__", 2)[-1])
        text = skill.read_text(errors="replace")
        match = re.search(r"^name:\s*['\"]?([^'\"\n]+)", text, re.M)
        if match:
            names.add(match.group(1).strip())
    return names


def source_shingles() -> list[tuple[Path, set[tuple[str, ...]]]]:
    if not SOURCE_ROOT.exists():
        if os.environ.get("ALLOW_MISSING_SOURCE_CORPUS") == "1":
            return []
        fail(f"source corpus not found: {SOURCE_ROOT}")
    source_files = list(SOURCE_ROOT.glob("*/*/SKILL.md"))
    if not source_files:
        fail(f"source corpus contains no SKILL.md files: {SOURCE_ROOT}")
    output = []
    for skill in source_files:
        output.append((skill, shingles(skill.read_text(errors="replace"))))
    return output


def source_line_sets() -> list[tuple[Path, set[str]]]:
    if not SOURCE_ROOT.exists():
        if os.environ.get("ALLOW_MISSING_SOURCE_CORPUS") == "1":
            return []
        fail(f"source corpus not found: {SOURCE_ROOT}")
    return [
        (skill, normalized_lines(skill.read_text(errors="replace")))
        for skill in SOURCE_ROOT.glob("*/*/SKILL.md")
    ]


def source_section_shingles() -> list[tuple[Path, set[tuple[str, ...]]]]:
    if not SOURCE_ROOT.exists():
        if os.environ.get("ALLOW_MISSING_SOURCE_CORPUS") == "1":
            return []
        fail(f"source corpus not found: {SOURCE_ROOT}")
    output = []
    for skill in SOURCE_ROOT.glob("*/*/SKILL.md"):
        for section in sections(skill.read_text(errors="replace")):
            output.append((skill, shingles(section, size=6)))
    return output


def validate_skill(
    path: Path,
    source_slug_set: set[str],
    source_sets: list[tuple[Path, set[tuple[str, ...]]]],
    source_lines: list[tuple[Path, set[str]]],
    source_section_sets: list[tuple[Path, set[tuple[str, ...]]]],
) -> str:
    text = path.read_text()
    fields = parse_frontmatter(text, path)
    folder_name = path.parent.name

    if fields.get("name") != folder_name:
        fail(f"{path} frontmatter name does not match folder name")
    if "description" not in fields:
        fail(f"{path} is missing description")
    if not fields["description"].startswith("Use when"):
        fail(f"{path} description must start with 'Use when'")
    if len(fields["description"]) > 650:
        fail(f"{path} description is too long for discovery")
    extras = set(fields) - {"name", "description"}
    if extras:
        fail(f"{path} has unsupported frontmatter keys: {sorted(extras)}")
    if set(fields) & FORBIDDEN_KEYS:
        fail(f"{path} uses source-style frontmatter keys")

    if "TODO" in text or "[TODO" in text:
        fail(f"{path} still contains scaffold placeholder text")
    for phrase in DENY_PHRASES:
        if phrase.lower() in text.lower():
            fail(f"{path} contains denied source phrase: {phrase}")

    headings = [h.strip() for h in re.findall(r"^##+\s+(.+)$", text, re.M)]
    bad_headings = SOURCE_STYLE_HEADINGS & set(headings)
    if bad_headings:
        fail(f"{path} uses source-style headings: {sorted(bad_headings)}")
    if not headings:
        fail(f"{path} has no body headings")

    own = shingles(text)
    if source_sets and own:
        worst_path = None
        worst_score = 0.0
        for source_path, source in source_sets:
            if not source:
                continue
            score = len(own & source) / len(own | source)
            if score > worst_score:
                worst_score = score
                worst_path = source_path
        if worst_score > 0.18:
            fail(f"{path} overlaps source too much ({worst_score:.3f}) with {worst_path}")

    own_lines = normalized_lines(text)
    for source_path, lines in source_lines:
        overlap = own_lines & lines
        if overlap:
            fail(f"{path} shares normalized prose lines with {source_path}: {sorted(overlap)[:2]}")

    for own_section in sections(text):
        own_section_shingles = shingles(own_section, size=6)
        if not own_section_shingles:
            continue
        for source_path, source_section in source_section_sets:
            if not source_section:
                continue
            containment = len(own_section_shingles & source_section) / len(own_section_shingles)
            if containment > 0.12:
                fail(f"{path} section overlaps source section too much ({containment:.3f}) with {source_path}")

    agents = path.parent / "agents" / "openai.yaml"
    if not agents.exists():
        fail(f"{path.parent} is missing agents/openai.yaml")
    agent_text = agents.read_text()
    if f"${folder_name}" not in agent_text:
        fail(f"{agents} default prompt must mention ${folder_name}")


def main() -> None:
    found = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name != "goal"}
    missing = EXPECTED_MARKETING_SKILLS - found
    unexpected = found - EXPECTED_MARKETING_SKILLS
    if missing:
        fail(f"missing expected marketing skills: {sorted(missing)}")
    if unexpected:
        fail(f"unexpected marketing skills: {sorted(unexpected)}")
    if not (10 <= len(found) <= 30):
        fail(f"expected 10-30 marketing skills, found {len(found)}")

    source_slug_set = source_names()
    source_sets = source_shingles()
    source_lines = source_line_sets()
    source_section_sets = source_section_shingles()
    for name in sorted(found):
        validate_skill(
            SKILLS_DIR / name / "SKILL.md",
            source_slug_set,
            source_sets,
            source_lines,
            source_section_sets,
        )

    print(f"OK: validated {len(found)} original marketing skills")


if __name__ == "__main__":
    main()
