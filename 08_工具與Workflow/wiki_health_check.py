#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from collections import Counter, defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any

WIKI_FOLDERS = [
    "00_總覽",
    "01_核心概念",
    "02_方法學",
    "03_疾病與臨床主題",
    "04_CPET",
    "05_Exercise_Physiology",
    "06_Gait_Biomechanics",
    "07_Pediatric_Development",
    "08_工具與Workflow",
    "09_來源摘要",
]

FRONTMATTER_REQUIRED = [
    "title",
    "created",
    "updated",
    "type",
    "domain",
    "tags",
    "source_tier",
    "evidence_level",
    "confidence",
    "contested",
    "contradictions",
]

PAGE_TYPES_REQUIRING_SOURCES = {"overview", "concept", "method", "clinical", "workflow", "query"}
CONTRADICTION_PATTERNS = [
    r"conflicting findings",
    r"conflicting evidence",
    r"results? (?:are|were) mixed",
    r"inconsistent findings",
    r"remain[s]? controversial",
    r"still controversial",
    r"仍有爭議",
    r"存在爭議",
    r"尚無定論",
    r"結果不一致",
    r"互相矛盾",
    r"conflict(?:ing)?",
]
KIND_PRIORITY = {"contradiction": 0, "stale": 1, "missing_core": 2, "backlog": 3}


@dataclass
class WikiPage:
    abs_path: Path
    rel_path: str
    section: str
    frontmatter: dict[str, Any]
    body: str
    lines: int
    links: list[str]
    outbound_existing: list[str]


def choose_existing_path(candidates: list[Path], exists_fn: Callable[[Path], bool] | None = None) -> Path:
    exists = exists_fn or (lambda path: path.exists())
    for candidate in candidates:
        if exists(candidate):
            return candidate
    return candidates[0]


def detect_default_roots(
    script_path: Path | None = None,
    exists_fn: Callable[[Path], bool] | None = None,
) -> tuple[Path, Path]:
    script_path = script_path or Path(__file__).resolve()
    script_wiki_root = script_path.parent.parent
    wiki_root = choose_existing_path(
        [Path(r"C:\知識百科"), Path("/mnt/c/知識百科"), script_wiki_root],
        exists_fn,
    )
    raw_root = choose_existing_path(
        [Path(r"C:\原始資料"), Path("/mnt/c/原始資料")],
        exists_fn,
    )
    return wiki_root, raw_root


def normalize_stem(name: str) -> str:
    stem = Path(name).stem
    stem = stem.lower()
    stem = re.sub(r"\.md$|\.pdf$|\.txt$", "", stem)
    stem = re.sub(r"^\d+\s*(?:[-_.]\s*)?(?=[a-z\u4e00-\u9fff])", "", stem)
    stem = re.sub(r"\(\d+\)$", "", stem)
    stem = re.sub(r"的副本$", "", stem)
    stem = re.sub(r"\b(?:pdf|txt|md)\b", "", stem)
    stem = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", stem)
    stem = re.sub(r"uptodate$", "", stem)
    return stem


def normalize_raw_reference(raw_ref: str, raw_root: Path) -> str | None:
    raw_ref = raw_ref.strip().strip("`").strip()
    if not raw_ref:
        return None

    windows_root = PureWindowsPath(str(raw_root))
    windows_ref = PureWindowsPath(raw_ref)
    if windows_ref.parts[: len(windows_root.parts)] == windows_root.parts:
        rel_parts = windows_ref.parts[len(windows_root.parts) :]
        return PurePosixPath(*rel_parts).as_posix() if rel_parts else None

    posix_root = PurePosixPath(raw_root.as_posix())
    posix_ref = PurePosixPath(raw_ref.replace("\\", "/"))
    if posix_ref.parts[: len(posix_root.parts)] == posix_root.parts:
        rel_parts = posix_ref.parts[len(posix_root.parts) :]
        return PurePosixPath(*rel_parts).as_posix() if rel_parts else None

    # Accept legacy wiki notation like `原始資料/foo/bar.md` in addition to absolute raw-root paths.
    raw_root_name = raw_root.name
    if windows_ref.parts and windows_ref.parts[0] == raw_root_name:
        rel_parts = windows_ref.parts[1:]
        return PurePosixPath(*rel_parts).as_posix() if rel_parts else None
    if posix_ref.parts and posix_ref.parts[0] == raw_root_name:
        rel_parts = posix_ref.parts[1:]
        return PurePosixPath(*rel_parts).as_posix() if rel_parts else None

    return None


def extract_explicit_raw_sources(page: WikiPage, raw_root: Path) -> set[str]:
    refs = set()
    if page.section != "09_來源摘要":
        return refs
    for match in re.finditer(r"原始檔：`([^`]+)`", page.body):
        rel = normalize_raw_reference(match.group(1), raw_root)
        if rel:
            refs.add(rel)
    return refs


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, flags=re.S)
    if not match:
        return {}, text
    raw_frontmatter, body = match.groups()
    result: dict[str, Any] = {}
    current_key = None
    for raw_line in raw_frontmatter.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("  - ") and current_key:
            result.setdefault(current_key, [])
            if not isinstance(result[current_key], list):
                result[current_key] = [result[current_key]]
            result[current_key].append(line[4:].strip())
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "":
            result[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                result[key] = []
            else:
                result[key] = [item.strip().strip("'\"") for item in inner.split(",")]
        elif value.lower() == "true":
            result[key] = True
        elif value.lower() == "false":
            result[key] = False
        elif re.fullmatch(r"\d+", value):
            result[key] = int(value)
        else:
            result[key] = value.strip("'\"")
    return result, body


def extract_wikilinks(text: str) -> list[str]:
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def link_candidates(raw_link: str, page_rel_path: str) -> list[str]:
    link = raw_link.split("|", 1)[0].split("#", 1)[0].strip()
    if not link:
        return []
    if not link.endswith(".md"):
        link = f"{link}.md"

    candidates = []
    base = posixpath.dirname(page_rel_path)
    if link.startswith("../") or link.startswith("./"):
        candidates.append(posixpath.normpath(posixpath.join(base, link)))
        return candidates

    if "/" in link:
        candidates.append(posixpath.normpath(link))
        return candidates

    candidates.append(posixpath.normpath(posixpath.join(base, link)))
    candidates.append(posixpath.normpath(link))
    return candidates


def iter_wiki_pages(wiki_root: Path) -> list[WikiPage]:
    pages: list[WikiPage] = []
    for folder in WIKI_FOLDERS:
        root = wiki_root / folder
        if not root.exists():
            continue
        for abs_path in sorted(root.rglob("*.md")):
            if abs_path.name.startswith("health_check_report"):
                continue
            rel_path = abs_path.relative_to(wiki_root).as_posix()
            text = abs_path.read_text(encoding="utf-8")
            frontmatter, body = parse_frontmatter(text)
            links = extract_wikilinks(body)
            pages.append(
                WikiPage(
                    abs_path=abs_path,
                    rel_path=rel_path,
                    section=folder,
                    frontmatter=frontmatter,
                    body=body,
                    lines=len(text.splitlines()),
                    links=links,
                    outbound_existing=[],
                )
            )
    return pages


def parse_index_links(index_text: str) -> set[str]:
    links = set()
    for line in index_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("- [["):
            continue
        for link in extract_wikilinks(stripped):
            target = link.split("|", 1)[0].split("#", 1)[0].strip()
            if not target:
                continue
            if not target.endswith(".md"):
                target = f"{target}.md"
            links.add(posixpath.normpath(target))
    return links


def frontmatter_issues(page: WikiPage) -> list[str]:
    issues = []
    fm = page.frontmatter
    for field in FRONTMATTER_REQUIRED:
        if field not in fm:
            issues.append(f"missing:{field}")
    page_type = str(fm.get("type", ""))
    if page_type in PAGE_TYPES_REQUIRING_SOURCES and "sources" not in fm:
        issues.append("missing:sources")
    if isinstance(fm.get("tags"), list) and not fm.get("tags"):
        issues.append("empty:tags")
    if page_type != "source_summary" and count_non_source_links(page) < 2:
        issues.append("crosslinks:<2")
    return issues


def count_non_source_links(page: WikiPage) -> int:
    return sum(1 for target in page.outbound_existing if not target.startswith("09_來源摘要/"))


def infer_tier_from_raw_file(path: Path) -> int:
    lowered_name = path.name.lower()
    lowered_path = path.as_posix().lower()

    try:
        head = path.read_text(encoding="utf-8", errors="ignore")[:4000].lower()
    except OSError:
        head = ""

    tier1_tokens = ["uptodate", "guideline", "textbook", "chapter", "systematic", "meta-analysis", "meta analysis"]
    tier2_tokens = ["cdc", "nih", "who", "official", "education", "website", "web", "book"]
    commercial_tokens = ["runrepeat", "cut in half", "review"]

    if any(token in lowered_name for token in ["uptodate", "guideline"]) or any(token in head for token in tier1_tokens):
        return 1
    if any(token in lowered_path for token in ["runrepeat", "精選鞋子"]) or any(token in head for token in commercial_tokens):
        return 2
    if any(token in lowered_name for token in ["cdc", "official", "book"]) or any(token in head for token in tier2_tokens):
        return 2
    return 3


def infer_impact(kind: str, section: str = "") -> int:
    base = {"contradiction": 10, "stale": 8, "missing_core": 7, "backlog": 5}.get(kind, 1)
    if section in {"04_CPET", "05_Exercise_Physiology", "03_疾病與臨床主題"}:
        base += 1
    return base


def select_raw_verification_queue(candidates: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    ranked = sorted(
        candidates,
        key=lambda item: (
            int(item.get("tier", 99)),
            -int(item.get("impact", 0)),
            KIND_PRIORITY.get(str(item.get("kind", "backlog")), 99),
            str(item.get("id", "")),
        ),
    )
    return ranked[:limit]


def analyze_wiki(wiki_root: str | Path, raw_root: str | Path) -> dict[str, Any]:
    wiki_root = Path(wiki_root)
    raw_root = Path(raw_root)
    pages = iter_wiki_pages(wiki_root)
    page_map = {page.rel_path: page for page in pages}
    basename_map: defaultdict[str, list[str]] = defaultdict(list)
    for rel_path in page_map:
        basename_map[posixpath.basename(rel_path)].append(rel_path)

    inbound_map: dict[str, set[str]] = defaultdict(set)
    broken_links: list[dict[str, str]] = []
    missing_core_counter: Counter[str] = Counter()
    missing_core_sources: defaultdict[str, set[str]] = defaultdict(set)

    for page in pages:
        resolved_targets = []
        for raw_link in page.links:
            candidates = link_candidates(raw_link, page.rel_path)
            if not candidates:
                continue

            target = next((candidate for candidate in candidates if candidate in page_map), None)
            if target is None:
                basename = posixpath.basename(candidates[0])
                matches = basename_map.get(basename, [])
                if len(matches) == 1:
                    target = matches[0]

            if target is not None:
                inbound_map[target].add(page.rel_path)
                resolved_targets.append(target)
            else:
                broken_target = candidates[0]
                broken_links.append({"source": page.rel_path, "target": broken_target})
                if page.section == "09_來源摘要" and not broken_target.startswith("09_來源摘要/"):
                    missing_core_counter[broken_target] += 1
                    missing_core_sources[broken_target].add(page.rel_path)
        page.outbound_existing = resolved_targets

    orphans = []
    weakly_linked = []
    oversized_pages = []
    frontmatter_findings = []
    contradiction_candidates = []
    stale_candidates = []

    for page in pages:
        inbound_count = len(inbound_map.get(page.rel_path, set()))
        non_source_links = count_non_source_links(page)
        if inbound_count == 0:
            orphans.append(
                {
                    "path": page.rel_path,
                    "section": page.section,
                    "inbound": 0,
                    "outbound": len(page.outbound_existing),
                    "non_source_outbound": non_source_links,
                }
            )
        if len(page.outbound_existing) < 2 or non_source_links < 2:
            weakly_linked.append(
                {
                    "path": page.rel_path,
                    "section": page.section,
                    "outbound": len(page.outbound_existing),
                    "non_source_outbound": non_source_links,
                }
            )
        if page.lines > 200:
            oversized_pages.append({"path": page.rel_path, "lines": page.lines})
        issues = frontmatter_issues(page)
        if issues:
            frontmatter_findings.append({"path": page.rel_path, "issues": issues})

        fm = page.frontmatter
        page_updated = str(fm.get("updated", ""))
        sources = fm.get("sources") if isinstance(fm.get("sources"), list) else []
        if page.section != "09_來源摘要" and sources:
            newer_sources = []
            for source in sources:
                source_path = source if source.endswith(".md") else f"{source}"
                source_path = posixpath.normpath(source_path)
                source_page = page_map.get(source_path)
                if source_page:
                    source_updated = str(source_page.frontmatter.get("updated", ""))
                    if page_updated and source_updated and source_updated > page_updated:
                        newer_sources.append(source_path)
            if newer_sources:
                stale_candidates.append({"path": page.rel_path, "newer_sources": newer_sources})

        body_text = page.body
        body_lower = body_text.lower()
        contested = bool(fm.get("contested", False))
        contradictions = fm.get("contradictions") if isinstance(fm.get("contradictions"), list) else []
        page_type = str(fm.get("type", ""))
        has_conflict_pattern = any(re.search(pattern, body_text, flags=re.I) for pattern in CONTRADICTION_PATTERNS)
        if page_type != "workflow" and has_conflict_pattern:
            if not contested and not contradictions:
                contradiction_candidates.append(
                    {
                        "path": page.rel_path,
                        "reason": "body_contains_conflict_language_without_frontmatter_flag",
                    }
                )

    index_path = wiki_root / "index.md"
    index_text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    index_links = parse_index_links(index_text)
    missing_from_index = [{"path": page.rel_path} for page in pages if page.rel_path not in index_links]
    index_missing_files = [{"path": link} for link in sorted(index_links) if link not in page_map]

    raw_backlog = []
    summary_stems = {normalize_stem(page.rel_path) for page in pages if page.section == "09_來源摘要"}
    summary_raw_paths = set()
    for page in pages:
        summary_raw_paths.update(extract_explicit_raw_sources(page, raw_root))
    if raw_root.exists():
        for path in sorted(raw_root.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".pdf", ".txt"}:
                continue
            if path.parent == raw_root and path.name.lower() == "readme.md":
                continue
            rel_path = path.relative_to(raw_root).as_posix()
            if rel_path in summary_raw_paths:
                continue
            stem = normalize_stem(path.name)
            if not stem or stem in summary_stems:
                continue
            raw_backlog.append(
                {
                    "path": rel_path,
                    "stem": Path(path.name).stem,
                    "tier": infer_tier_from_raw_file(path),
                }
            )

    missing_core_topics = []
    for target, count in missing_core_counter.items():
        if count >= 2 and target not in page_map:
            missing_core_topics.append(
                {
                    "target": target,
                    "mentions": count,
                    "source_pages": sorted(missing_core_sources[target]),
                }
            )

    verification_candidates = []
    for item in stale_candidates:
        verification_candidates.append(
            {
                "id": item["path"],
                "kind": "stale",
                "tier": 1,
                "impact": infer_impact("stale", item["path"].split("/", 1)[0]),
                "path": item["path"],
            }
        )
    for item in contradiction_candidates:
        verification_candidates.append(
            {
                "id": item["path"],
                "kind": "contradiction",
                "tier": 1,
                "impact": infer_impact("contradiction", item["path"].split("/", 1)[0]),
                "path": item["path"],
            }
        )
    for item in missing_core_topics:
        verification_candidates.append(
            {
                "id": item["target"],
                "kind": "missing_core",
                "tier": 1,
                "impact": infer_impact("missing_core"),
                "path": item["target"],
            }
        )
    for item in raw_backlog:
        verification_candidates.append(
            {
                "id": item["stem"],
                "kind": "backlog",
                "tier": item["tier"],
                "impact": infer_impact("backlog"),
                "path": item["path"],
            }
        )

    raw_verification_queue = select_raw_verification_queue(verification_candidates, limit=5)

    report = {
        "wiki_root": str(wiki_root),
        "raw_root": str(raw_root),
        "generated_on": str(date.today()),
        "summary": {
            "pages_scanned": len(pages),
            "orphans": len(orphans),
            "weakly_linked_pages": len(weakly_linked),
            "broken_links": len(broken_links),
            "missing_from_index": len(missing_from_index),
            "index_missing_files": len(index_missing_files),
            "frontmatter_issues": len(frontmatter_findings),
            "oversized_pages": len(oversized_pages),
            "stale_candidates": len(stale_candidates),
            "contradiction_candidates": len(contradiction_candidates),
            "missing_core_topics": len(missing_core_topics),
            "raw_backlog": len(raw_backlog),
            "raw_verification_queue": len(raw_verification_queue),
        },
        "orphans": sorted(orphans, key=lambda x: x["path"]),
        "weakly_linked_pages": sorted(weakly_linked, key=lambda x: x["path"]),
        "broken_links": sorted(broken_links, key=lambda x: (x["source"], x["target"])),
        "missing_from_index": sorted(missing_from_index, key=lambda x: x["path"]),
        "index_missing_files": sorted(index_missing_files, key=lambda x: x["path"]),
        "frontmatter_issues": sorted(frontmatter_findings, key=lambda x: x["path"]),
        "oversized_pages": sorted(oversized_pages, key=lambda x: (-x["lines"], x["path"])),
        "stale_candidates": sorted(stale_candidates, key=lambda x: x["path"]),
        "contradiction_candidates": sorted(contradiction_candidates, key=lambda x: x["path"]),
        "missing_core_topics": sorted(missing_core_topics, key=lambda x: (-x["mentions"], x["target"])),
        "raw_backlog": sorted(raw_backlog, key=lambda x: (x["tier"], x["stem"].lower())),
        "raw_verification_queue": raw_verification_queue,
    }
    return report


def markdown_report(report: dict[str, Any]) -> str:
    lines = []
    s = report["summary"]
    lines.append("# Wiki health check report")
    lines.append("")
    lines.append(f"- generated_on: {report['generated_on']}")
    lines.append(f"- pages_scanned: {s['pages_scanned']}")
    lines.append(f"- orphans: {s['orphans']}")
    lines.append(f"- weakly_linked_pages: {s['weakly_linked_pages']}")
    lines.append(f"- broken_links: {s['broken_links']}")
    lines.append(f"- stale_candidates: {s['stale_candidates']}")
    lines.append(f"- contradiction_candidates: {s['contradiction_candidates']}")
    lines.append(f"- missing_core_topics: {s['missing_core_topics']}")
    lines.append(f"- raw_backlog: {s['raw_backlog']}")
    lines.append(f"- raw_verification_queue: {s['raw_verification_queue']} (cap: 5)")
    lines.append("")

    def add_section(title: str, items: list[dict[str, Any]], formatter) -> None:
        lines.append(f"## {title}")
        if not items:
            lines.append("- none")
        else:
            for item in items:
                lines.append(formatter(item))
        lines.append("")

    add_section("Orphans", report["orphans"], lambda x: f"- {x['path']} | outbound={x['outbound']} | non_source_outbound={x['non_source_outbound']}")
    add_section("Weakly linked pages", report["weakly_linked_pages"], lambda x: f"- {x['path']} | outbound={x['outbound']} | non_source_outbound={x['non_source_outbound']}")
    add_section("Broken links", report["broken_links"], lambda x: f"- {x['source']} -> {x['target']}")
    add_section("Missing from index", report["missing_from_index"], lambda x: f"- {x['path']}")
    add_section("Index points to missing files", report["index_missing_files"], lambda x: f"- {x['path']}")
    add_section("Frontmatter issues", report["frontmatter_issues"], lambda x: f"- {x['path']} | {', '.join(x['issues'])}")
    add_section("Oversized pages", report["oversized_pages"], lambda x: f"- {x['path']} | lines={x['lines']}")
    add_section("Stale candidates", report["stale_candidates"], lambda x: f"- {x['path']} | newer_sources={', '.join(x['newer_sources'])}")
    add_section("Contradiction candidates", report["contradiction_candidates"], lambda x: f"- {x['path']} | {x['reason']}")
    add_section("Missing core topics", report["missing_core_topics"], lambda x: f"- {x['target']} | mentions={x['mentions']} | source_pages={', '.join(x['source_pages'])}")
    add_section("Raw backlog", report["raw_backlog"], lambda x: f"- {x['path']} | tier={x['tier']}")
    add_section("Raw verification queue", report["raw_verification_queue"], lambda x: f"- {x['path']} | kind={x['kind']} | tier={x['tier']} | impact={x['impact']}")
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    default_wiki, default_raw = detect_default_roots()
    parser = argparse.ArgumentParser(description="Lint / health-check the medical wiki.")
    parser.add_argument("--wiki", default=str(default_wiki), help="Wiki root path")
    parser.add_argument("--raw", default=str(default_raw), help="Raw source root path")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    parser.add_argument("--output", help="Optional report output path")
    args = parser.parse_args()

    report = analyze_wiki(args.wiki, args.raw)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) if args.format == "json" else markdown_report(report)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
    else:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
