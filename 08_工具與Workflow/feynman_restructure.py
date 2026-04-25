from __future__ import annotations

import argparse
import os
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(r"C:\知識百科")
TODAY = "2026-04-24"
EXCLUDED_RELATIVE = {
    "index.md",
    "log.md",
    "SCHEMA.md",
    r"08_工具與Workflow\health_check_report_latest.md",
}
EXCLUDED_DIR_MARKERS = {".obsidian", "__pycache__", "tests"}

SECTION_ORDER = [
    "一句話定義",
    "核心機制",
    "臨床表現",
    "評估方式",
    "治療原則",
    "臨床決策點",
    "限制與未定論",
    "理解缺口",
    "臨床使用版",
    "來源",
    "相關頁面",
]


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            frontmatter = "\n".join(lines[: i + 1]).strip() + "\n"
            body = "\n".join(lines[i + 1 :]).lstrip("\n")
            return frontmatter, body
    return "", text


def update_frontmatter(frontmatter: str) -> str:
    if not frontmatter:
        return frontmatter
    if re.search(r"(?m)^updated:\s*.+$", frontmatter):
        frontmatter = re.sub(r"(?m)^updated:\s*.+$", f"updated: {TODAY}", frontmatter)
    return frontmatter


def parse_frontmatter_scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    return match.group(1).strip() if match else ""


def parse_frontmatter_list(frontmatter: str, key: str) -> list[str]:
    lines = frontmatter.splitlines()
    result: list[str] = []
    for i, line in enumerate(lines):
        if not line.startswith(f"{key}:"):
            continue
        rest = line.split(":", 1)[1].strip()
        if rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1].strip()
            if not inner:
                return []
            return [item.strip().strip("'\"") for item in inner.split(",") if item.strip()]
        if rest:
            return [rest.strip().strip("'\"")]
        j = i + 1
        while j < len(lines):
            candidate = lines[j]
            if candidate.startswith("  - "):
                result.append(candidate[4:].strip())
                j += 1
                continue
            if candidate.startswith("    "):
                j += 1
                continue
            break
        return result
    return result


def parse_title_and_sections(body: str, fallback_title: str) -> tuple[str, str, list[tuple[str, str]]]:
    lines = body.splitlines()
    title = fallback_title
    idx = 0
    while idx < len(lines):
        if lines[idx].startswith("# "):
            title = lines[idx][2:].strip()
            idx += 1
            break
        idx += 1
    remaining = lines[idx:]
    preamble: list[str] = []
    sections: list[tuple[str, str]] = []
    current_heading = ""
    current_lines: list[str] = []
    seen_section = False

    for line in remaining:
        if line.startswith("## "):
            if seen_section:
                sections.append((current_heading, "\n".join(current_lines).strip()))
            elif preamble:
                preamble_text = "\n".join(preamble).strip()
                if preamble_text:
                    sections.append(("_preamble", preamble_text))
            seen_section = True
            current_heading = line[3:].strip()
            current_lines = []
            continue
        if seen_section:
            current_lines.append(line)
        else:
            preamble.append(line)

    if seen_section:
        sections.append((current_heading, "\n".join(current_lines).strip()))
    elif preamble:
        preamble_text = "\n".join(preamble).strip()
        if preamble_text:
            sections.append(("_preamble", preamble_text))

    return title, "\n".join(preamble).strip(), sections


def section_key(name: str) -> str:
    key = name.strip().lower()
    key = key.replace("／", "/")
    key = re.sub(r"\s+", "", key)
    return key


def classify_section(name: str, page_type: str) -> str:
    key = section_key(name)
    if key in {"一句話定義", "一句話總結"}:
        return "definition"
    if key in {"相關頁面", "相關wiki頁面"}:
        return "related"
    if key == "書目":
        return "source"
    if any(token in key for token in ["限制", "爭議", "caveat", "衝突", "證據層級", "不該過度延伸"]):
        return "limits"
    if any(token in key for token in ["評估", "history", "physical", "檢查", "影像", "量表", "測試", "診斷", "diagnosis", "篩檢", "可靠性", "何時要懷疑", "常見differential"]):
        return "evaluation"
    if any(token in key for token in ["治療", "管理", "處方", "復健", "介入", "returntosport/work", "preparticipation", "選用原則", "選配原則", "急性處置", "輔具", "program"]):
        return "treatment"
    if any(token in key for token in ["臨床", "症狀", "紅旗", "分型", "重要性", "為何重要", "實務提醒", "常見錯誤", "eligibility", "核心用途"]):
        return "clinical"
    if any(token in key for token in ["反對論點", "結論", "wiki的意義", "這篇對wiki主幹的價值", "在本wiki的定位", "真正回答什麼問題"]):
        return "decision"
    if any(token in key for token in ["主要貢獻", "核心內容拆解", "先用白話講懂"]):
        return "mechanism"
    if key == "_preamble":
        return "mechanism"
    if any(token in key for token in ["機制", "概念", "框架", "原理", "pathogenesis", "調控", "數學", "生理意義", "工具", "核心", "主軸", "模組", "方法學", "主要結果", "關係", "總覽", "workflow"]):
        return "mechanism"
    if page_type in {"clinical"}:
        return "clinical"
    return "mechanism"


def render_items(items: list[tuple[str, str]], placeholder: str) -> str:
    blocks: list[str] = []
    for heading, content in items:
        content = content.strip()
        if not content:
            continue
        if heading == "_preamble":
            blocks.append(content)
        else:
            blocks.append(f"### {heading}\n\n{content}")
    if not blocks:
        return placeholder
    return "\n\n".join(blocks)


def bulletize(items: list[str]) -> str:
    cleaned = [item.strip() for item in items if item and item.strip()]
    if not cleaned:
        return ""
    return "\n".join(f"- {item}" for item in cleaned)


def collect_contradictions(frontmatter: str) -> list[str]:
    lines = frontmatter.splitlines()
    contradictions: list[str] = []
    in_block = False
    for line in lines:
        if line.startswith("contradictions:"):
            in_block = True
            continue
        if in_block and line.startswith("  - "):
            contradictions.append(line[4:].strip())
            continue
        if in_block and not line.startswith("  "):
            break
    return contradictions


def default_definition(title: str, page_type: str) -> str:
    if page_type == "source_summary":
        return f"這頁整理「{title}」這份來源真正能教給住院醫師的主架構，並把可直接用於臨床決策的部分拆開。"
    if page_type == "workflow":
        return f"這頁說明「{title}」的操作骨架，目標是把流程寫成可執行而非只可閱讀。"
    if page_type == "overview":
        return f"這頁用單一導航主題整理「{title}」，目的是先找到骨架，再往下連到細節頁。"
    if page_type == "method":
        return f"「{title}」是一個方法學主題，重點不在背名詞，而在知道這個方法何時能改變評估或處置。"
    if page_type == "concept":
        return f"「{title}」是一個核心概念頁，重點是把名詞、機制與實際判讀連起來。"
    return f"「{title}」是一個臨床主題，重點是把概念轉成可實際使用的判斷與處置。"


def section_placeholder(section_name: str, page_type: str) -> str:
    placeholders = {
        "核心機制": "- 目前頁面尚未把已知與機制拆開；需回源補成可教學的病理生理或方法原理。",
        "臨床表現": "- 目前頁面尚未整理出可直接辨識的症狀、檢查發現或 red flags。",
        "評估方式": "- 目前頁面尚未整理出 History、Physical examination、Scale / test、Imaging / lab 的實際用法。",
        "治療原則": "- 目前頁面尚未整理出 Non-pharmacologic、Pharmacologic、Injection / procedure、Rehabilitation program 的決策順序。",
        "臨床決策點": "- 目前頁面尚未整理出 treatment threshold、referral threshold 與不該做的事。",
        "限制與未定論": "- 目前頁面尚未明確寫出證據限制、教材未講清楚處或不同來源可能衝突之處。",
    }
    if section_name == "臨床表現" and page_type in {"workflow", "overview"}:
        return "- 本頁不是疾病頁；此處應改讀為常見使用情境、常見失敗模式與需要警覺的流程 red flags。"
    if section_name == "治療原則" and page_type in {"concept", "source_summary"}:
        return "- 本頁以概念或來源為主；若要進入真正 treatment plan，需連回對應臨床頁。"
    return placeholders[section_name]


def generate_gaps(title: str, page_type: str, buckets: dict[str, list[tuple[str, str]]]) -> list[str]:
    gaps: list[str] = []
    if page_type == "clinical":
        gaps.extend(
            [
                f"{title} 最容易和哪幾個 mimic / differential 混淆？差異機制是什麼？",
                "哪些 bedside finding 真的會改變 treatment threshold，而不是只增加診斷把握？",
                "哪些量表或影像異常和功能障礙不一定一致？原因是什麼？",
            ]
        )
    elif page_type == "concept":
        gaps.extend(
            [
                f"{title} 和最相近、最常被混用的概念差在哪？",
                "這個指標或概念反映的是直接機制，還是只是 operational proxy？",
                "在什麼測試條件或族群下，這個概念最容易被錯用或外推失真？",
            ]
        )
    elif page_type == "method":
        gaps.extend(
            [
                f"{title} 量到的是什麼，不是什麼？",
                "這個方法最常見的 protocol pitfall 是什麼？",
                "如果結果異常，哪些情況不能直接跳到 treatment conclusion？",
            ]
        )
    elif page_type == "source_summary":
        gaps.extend(
            [
                "這份來源哪些部分是在建立主框架，哪些部分只是作者的解釋或延伸？",
                "若 guideline、review 或新版 textbook 和本來源不同，主幹應如何更新？",
                "這份來源最值得直接回填到哪個主題頁，哪些段落不該過度外推？",
            ]
        )
    else:
        gaps.extend(
            [
                f"{title} 的核心輸出是什麼？如果要教給住院醫師，最少要保留哪三個步驟？",
                "哪些情況代表這個流程或總覽頁仍然不夠可執行？",
                "這頁和相鄰主題頁的邊界在哪裡？",
            ]
        )

    if not buckets["evaluation"]:
        gaps.append("目前缺少完整評估框架：History、Physical examination、Scale / test、Imaging / lab 仍需補強。")
    if not buckets["treatment"]:
        gaps.append("目前缺少明確處置順序：何時觀察、何時介入、何時轉介仍需補強。")
    if not buckets["clinical"]:
        gaps.append("目前缺少 bedside 可辨識表現：症狀、檢查發現或 red flags 仍需補強。")
    return gaps[:5]


def generate_clinical_use(title: str, page_type: str) -> list[str]:
    if page_type == "clinical":
        return [
            f"若病人的症狀、檢查與功能限制符合 {title} 的框架，先用本頁的 History / Physical / red flags 決定是否需要影像、介入或轉介。",
            "若只有名詞相像、但機制或時序對不上，先回 differential，不要直接套用診斷與治療。",
        ]
    if page_type == "concept":
        return [
            f"若要把 {title} 用在 bedside 或運動處方，先確認它回答的是哪一個機制或強度邊界，再決定能否改變評估與處置。",
            "若這個概念無法改變你的臨床決策，就不要只為了名詞完整而硬套到病人身上。",
        ]
    if page_type == "method":
        return [
            f"若 {title} 不能改變診斷、風險分層或 treatment plan，就不該例行使用。",
            "先界定問題、輸入條件與輸出格式，再執行方法，否則結果很容易只有數字沒有決策價值。",
        ]
    if page_type == "source_summary":
        return [
            "若要更新主題頁，先用這份來源建立主框架，再用 guideline / review 校正 treatment threshold 與爭議點。",
            "不要把單一 textbook chapter 或單篇文章的語句直接當成全域共識；先看它在整個證據層級中的位置。",
        ]
    if page_type == "workflow":
        return [
            f"若 {title} 不能縮短查找、整理或衝突處理時間，代表流程描述仍然不夠可執行。",
            "每一步都要能回答下一個實際動作是什麼，否則就只是說明文件，不是 workflow。",
        ]
    return [
        f"先把 {title} 當成導航頁使用：用它找到主幹，再往下連到能直接改變評估或處置的頁面。",
        "若這頁無法幫你快速縮小範圍，代表拆頁仍不夠單一概念。",
    ]


def build_source_section(
    frontmatter: str,
    source_items: list[tuple[str, str]],
) -> str:
    parts: list[str] = []
    sources = parse_frontmatter_list(frontmatter, "sources")
    if sources:
        parts.append("### 來源摘要連結\n\n" + "\n".join(f"- [[{source[:-3]}]]" if source.endswith(".md") else f"- {source}" for source in sources))
    source_tier = parse_frontmatter_scalar(frontmatter, "source_tier")
    evidence_level = parse_frontmatter_scalar(frontmatter, "evidence_level")
    confidence = parse_frontmatter_scalar(frontmatter, "confidence")
    meta_lines = []
    if source_tier:
        meta_lines.append(f"來源層級：{source_tier}")
    if evidence_level:
        meta_lines.append(f"evidence_level：{evidence_level}")
    if confidence:
        meta_lines.append(f"confidence：{confidence}")
    if meta_lines:
        parts.append("### 證據標記\n\n" + bulletize(meta_lines))
    if source_items:
        parts.append(render_items(source_items, "- 目前未保留原始書目說明。"))
    if not parts:
        return "- 目前頁面未標示可追溯來源。"
    return "\n\n".join(parts)


def build_related_section(related_items: list[tuple[str, str]]) -> str:
    rendered = render_items(related_items, "")
    return rendered if rendered else "- 目前頁面尚未整理相關頁面連結。"


def convert_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(original)
    title_in_frontmatter = parse_frontmatter_scalar(frontmatter, "title") or path.stem
    page_type = parse_frontmatter_scalar(frontmatter, "type") or "clinical"
    title, preamble, sections = parse_title_and_sections(body, title_in_frontmatter)

    buckets: dict[str, list[tuple[str, str]]] = defaultdict(list)
    definition = ""
    if preamble:
        buckets["mechanism"].append(("_preamble", preamble))

    for heading, content in sections:
        category = classify_section(heading, page_type)
        if category == "definition":
            if not definition and content.strip():
                definition = content.strip()
            else:
                buckets["mechanism"].append((heading, content))
            continue
        buckets[category].append((heading, content))

    if not definition:
        definition = default_definition(title, page_type)

    contradictions = collect_contradictions(frontmatter)
    if contradictions:
        contradiction_block = bulletize(contradictions)
        buckets["limits"].append(("frontmatter contradictions", contradiction_block))

    new_sections: dict[str, str] = {}
    new_sections["一句話定義"] = definition.strip()
    new_sections["核心機制"] = render_items(
        buckets["mechanism"],
        section_placeholder("核心機制", page_type),
    )
    new_sections["臨床表現"] = render_items(
        buckets["clinical"],
        section_placeholder("臨床表現", page_type),
    )
    new_sections["評估方式"] = render_items(
        buckets["evaluation"],
        section_placeholder("評估方式", page_type),
    )
    new_sections["治療原則"] = render_items(
        buckets["treatment"],
        section_placeholder("治療原則", page_type),
    )
    decision_parts: list[str] = []
    rendered_decisions = render_items(buckets["decision"], "")
    if rendered_decisions:
        decision_parts.append(rendered_decisions)
    decision_parts.append(
        bulletize(
            [
                "什麼情況要治療？先看是否真的改變 pain、function、safety、participation 或訓練輸出。",
                "什麼情況要轉介？遇到 red flags、診斷不確定、需要程序性介入或超出本頁可處理範圍時。",
                "什麼情況不該做？當證據不足、機制不合、風險高於預期收益，或結果不會改變決策時。",
            ]
        )
    )
    new_sections["臨床決策點"] = "\n\n".join(part for part in decision_parts if part.strip())
    new_sections["限制與未定論"] = render_items(
        buckets["limits"],
        section_placeholder("限制與未定論", page_type),
    )
    new_sections["理解缺口"] = bulletize(generate_gaps(title, page_type, buckets))
    new_sections["臨床使用版"] = bulletize(generate_clinical_use(title, page_type))
    new_sections["來源"] = build_source_section(frontmatter, buckets["source"])
    new_sections["相關頁面"] = build_related_section(buckets["related"])

    updated_frontmatter = update_frontmatter(frontmatter)
    rendered_sections = []
    for section_name in SECTION_ORDER:
        rendered_sections.append(f"## {section_name}\n\n{new_sections[section_name].strip()}")

    new_body = f"# {title}\n\n" + "\n\n".join(rendered_sections).strip() + "\n"
    new_text = (updated_frontmatter + "\n" if updated_frontmatter else "") + new_body

    if new_text != original:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def iter_target_files(root: Path) -> list[Path]:
    targets: list[Path] = []
    for current_root, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIR_MARKERS]
        for filename in filenames:
            if not filename.lower().endswith(".md"):
                continue
            path = Path(current_root) / filename
            rel = str(path.relative_to(root))
            if rel in EXCLUDED_RELATIVE:
                continue
            targets.append(path)
    return sorted(targets)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root)
    files = iter_target_files(root)
    if args.limit:
        files = files[: args.limit]

    changed = 0
    for path in files:
        original = path.read_text(encoding="utf-8")
        frontmatter, body = split_frontmatter(original)
        title_in_frontmatter = parse_frontmatter_scalar(frontmatter, "title") or path.stem
        page_type = parse_frontmatter_scalar(frontmatter, "type") or "clinical"
        title, preamble, sections = parse_title_and_sections(body, title_in_frontmatter)
        # Run conversion once to compute the result, optionally revert for dry-run.
        if args.dry_run:
            tmp_path = path
            if convert_file(tmp_path):
                changed += 1
                tmp_path.write_text(original, encoding="utf-8")
            continue
        if convert_file(path):
            changed += 1

    print(f"processed={len(files)} changed={changed} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
