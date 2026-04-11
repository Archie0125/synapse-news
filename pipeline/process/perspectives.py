"""Load distilled perspective skills (女娲.skill format) and compose them into
a prompt-injectable editorial DNA block.

Reads SKILL.md files from .claude/skills/<name>-perspective/ and extracts the
three sections that matter for content generation: mental models, decision
heuristics, and expression DNA. Everything else (timeline, research sources,
role-play rules) is discarded to keep token cost reasonable.

To extend to other phases (generate_analysis, threads), call
`compose_perspectives(config['perspectives'][phase])` and concatenate the
result onto the base prompt — same pattern as summarize.py.
"""

import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

SKILLS_DIR = Path(".claude/skills")

# Short name -> on-disk skill directory name
_NAME_MAP = {
    "mrbeast": "mrbeast-perspective",
    "feynman": "feynman-perspective",
    "paul-graham": "paul-graham-perspective",
    "pg": "paul-graham-perspective",
    "zhang-yiming": "zhang-yiming-perspective",
    "zhangyiming": "zhang-yiming-perspective",
}

# H2 section headers we care about. First match wins per category — some skills
# use "核心心智模型（N个）" so we match by prefix.
_SECTION_PATTERNS = {
    "mental_models": [r"^##\s*核心心智模型", r"^##\s*心智模型"],
    "heuristics": [r"^##\s*决策启发式", r"^##\s*启发式"],
    "expression": [r"^##\s*表达DNA", r"^##\s*内容创造公式手册"],
}

# Maximum number of H3 subsections to keep per section. Keeps token cost flat.
_MAX_ITEMS = {"mental_models": 4, "heuristics": 6, "expression": 3}

_CACHE: dict[str, str] = {}


def _resolve_skill_dir(name: str) -> Path | None:
    key = name.strip().lower()
    dirname = _NAME_MAP.get(key, key)
    path = SKILLS_DIR / dirname
    if not path.exists():
        logger.warning(f"Perspective skill not found: {name} (looked in {path})")
        return None
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        logger.warning(f"SKILL.md missing for perspective: {name}")
        return None
    return skill_md


def _split_sections(text: str) -> dict[str, str]:
    """Slice the markdown body into top-level H2 sections keyed by header text."""
    sections: dict[str, str] = {}
    current_header: str | None = None
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current_header is not None:
                sections[current_header] = "\n".join(current_lines).strip()
            current_header = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_header is not None:
        sections[current_header] = "\n".join(current_lines).strip()
    return sections


def _find_section(sections: dict[str, str], patterns: list[str]) -> str | None:
    for header, body in sections.items():
        full_line = f"## {header}"
        for pat in patterns:
            if re.match(pat, full_line):
                return body
    return None


def _compress_section(body: str, max_items: int) -> str:
    """Keep only H3 title + the first `**一句话**：` line (or first non-empty
    paragraph) for each subsection. Caps at max_items."""
    blocks: list[tuple[str, list[str]]] = []
    current_title: str | None = None
    current_body: list[str] = []
    for line in body.splitlines():
        if line.startswith("### "):
            if current_title is not None:
                blocks.append((current_title, current_body))
            current_title = line[4:].strip()
            current_body = []
        else:
            if current_title is not None:
                current_body.append(line)
    if current_title is not None:
        blocks.append((current_title, current_body))

    out: list[str] = []
    for title, lines in blocks[:max_items]:
        gist = _extract_gist(lines)
        if gist:
            out.append(f"- **{title}** — {gist}")
        else:
            out.append(f"- **{title}**")
    return "\n".join(out) if out else body[:400]


def _extract_gist(lines: list[str]) -> str:
    """Prefer `**一句话**：...` lines; fall back to first meaningful paragraph."""
    for line in lines:
        m = re.match(r"\*\*一句话\*\*[:：]\s*(.+)", line.strip())
        if m:
            return m.group(1).strip()
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith(("---", "```", "**来源**", "**我的原话**", "**局限**", "**数据**")):
            continue
        stripped = re.sub(r"\*\*", "", stripped)
        if len(stripped) > 15:
            return stripped[:200]
    return ""


def load_perspective(name: str) -> str | None:
    """Return a compact markdown block for one perspective, or None if missing."""
    if name in _CACHE:
        return _CACHE[name]

    skill_md = _resolve_skill_dir(name)
    if skill_md is None:
        return None

    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError as e:
        logger.warning(f"Failed to read {skill_md}: {e}")
        return None

    sections = _split_sections(text)
    parts: list[str] = [f"### {name}"]

    mm = _find_section(sections, _SECTION_PATTERNS["mental_models"])
    if mm:
        parts.append("**Mental models:**\n" + _compress_section(mm, _MAX_ITEMS["mental_models"]))

    heur = _find_section(sections, _SECTION_PATTERNS["heuristics"])
    if heur:
        parts.append("**Decision heuristics:**\n" + _compress_section(heur, _MAX_ITEMS["heuristics"]))

    expr = _find_section(sections, _SECTION_PATTERNS["expression"])
    if expr:
        parts.append("**Expression DNA:**\n" + _compress_section(expr, _MAX_ITEMS["expression"]))

    if len(parts) == 1:
        logger.warning(f"Perspective {name} had no usable sections")
        return None

    result = "\n\n".join(parts)
    _CACHE[name] = result
    return result


def compose_perspectives(names: list[str]) -> str:
    """Compose multiple perspectives into a single prompt-injectable block.

    The returned text is designed to be appended to an existing system prompt.
    It explicitly frames the perspectives as thinking frameworks to INCORPORATE,
    not personas to ROLEPLAY — this preserves the caller's primary editorial voice.
    """
    if not names:
        return ""

    blocks = [load_perspective(n) for n in names]
    blocks = [b for b in blocks if b]
    if not blocks:
        return ""

    preamble = (
        "## Editorial DNA — thinking frameworks to apply\n\n"
        "Incorporate the following mental models and heuristics when you form "
        "takes and write TLDRs. Do NOT roleplay or quote these people. Do NOT "
        "mention their names in the output. Use their *frameworks* to sharpen "
        "your own editorial judgment — what to zoom in on, what angle to pick, "
        "how to make the opinion land."
    )
    return preamble + "\n\n" + "\n\n---\n\n".join(blocks)
