import importlib.util
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "wiki_health_check.py"


def load_module():
    spec = importlib.util.spec_from_file_location("wiki_health_check", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


class WikiHealthCheckTests(unittest.TestCase):
    def test_detect_default_roots_prefers_existing_windows_paths_then_script_root(self):
        module = load_module()
        fake_script = Path("/tmp/fake/08_工具與Workflow/wiki_health_check.py")

        existing_windows = {
            Path(r"C:\知識百科"),
            Path(r"C:\原始資料"),
        }
        wiki_root, raw_root = module.detect_default_roots(
            script_path=fake_script,
            exists_fn=lambda path: path in existing_windows,
        )
        self.assertEqual(wiki_root, Path(r"C:\知識百科"))
        self.assertEqual(raw_root, Path(r"C:\原始資料"))

        existing_script_only = {
            fake_script.parent.parent,
            Path("/mnt/c/原始資料"),
        }
        wiki_root, raw_root = module.detect_default_roots(
            script_path=fake_script,
            exists_fn=lambda path: path in existing_script_only,
        )
        self.assertEqual(wiki_root, fake_script.parent.parent)
        self.assertEqual(raw_root, Path("/mnt/c/原始資料"))

    def test_detects_orphans_weak_links_index_gaps_and_raw_backlog(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as wiki_dir, tempfile.TemporaryDirectory() as raw_dir:
            wiki = Path(wiki_dir)
            raw = Path(raw_dir)

            for folder in [
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
            ]:
                (wiki / folder).mkdir(parents=True, exist_ok=True)

            write(
                wiki / "SCHEMA.md",
                """
                # Schema
                """,
            )
            write(
                wiki / "log.md",
                """
                # Log
                ## [2026-04-23] create | init
                """,
            )
            write(
                wiki / "index.md",
                """
                # 索引
                ## 04 CPET
                - [[04_CPET/Page_A]] — page a
                ## 09 來源摘要
                - [[09_來源摘要/Source_One]] — source one
                """,
            )
            write(
                wiki / "04_CPET/Page_A.md",
                """
                ---
                title: Page A
                created: 2026-04-23
                updated: 2026-04-23
                type: concept
                domain: [CPET]
                tags: [a]
                sources: [09_來源摘要/Source_One.md]
                source_tier: 1
                evidence_level: consensus
                confidence: high
                contested: false
                contradictions: []
                ---

                [[04_CPET/Page_B]]
                """,
            )
            write(
                wiki / "04_CPET/Page_B.md",
                """
                ---
                title: Page B
                created: 2026-04-23
                updated: 2026-04-23
                type: concept
                domain: [CPET]
                tags: [b]
                sources: [09_來源摘要/Source_One.md]
                source_tier: 1
                evidence_level: consensus
                confidence: high
                contested: false
                contradictions: []
                ---

                [[04_CPET/Page_A]]
                """,
            )
            write(
                wiki / "04_CPET/Page_Orphan.md",
                """
                ---
                title: Page Orphan
                created: 2026-04-23
                updated: 2026-04-23
                type: concept
                domain: [CPET]
                tags: [orphan]
                sources: [09_來源摘要/Source_One.md]
                source_tier: 1
                evidence_level: consensus
                confidence: high
                contested: false
                contradictions: []
                ---

                [[04_CPET/Page_A]]
                """,
            )
            write(
                wiki / "09_來源摘要/Source_One.md",
                """
                ---
                title: Source One
                created: 2026-04-23
                updated: 2026-04-23
                type: source_summary
                domain: [CPET]
                tags: [summary]
                source_tier: 1
                evidence_level: consensus
                confidence: high
                contested: false
                contradictions: []
                ---

                [[04_CPET/Page_A]]
                """,
            )

            write(raw / "source-one.md", "x")
            write(raw / "new-review.md", "y")
            write(raw / "README.md", "raw staging readme\n")

            report = module.analyze_wiki(wiki, raw)

            orphan_paths = {item["path"] for item in report["orphans"]}
            weak_link_paths = {item["path"] for item in report["weakly_linked_pages"]}
            missing_index_paths = {item["path"] for item in report["missing_from_index"]}
            raw_backlog_stems = {item["stem"] for item in report["raw_backlog"]}

            self.assertIn("04_CPET/Page_Orphan.md", orphan_paths)
            self.assertIn("04_CPET/Page_A.md", weak_link_paths)
            self.assertIn("04_CPET/Page_B.md", missing_index_paths)
            self.assertIn("04_CPET/Page_Orphan.md", missing_index_paths)
            self.assertIn("new-review", raw_backlog_stems)
            self.assertNotIn("source-one", raw_backlog_stems)
            self.assertNotIn("readme", raw_backlog_stems)

    def test_normalize_stem_strips_chapter_prefix_and_copy_suffix(self):
        module = load_module()

        self.assertEqual(
            module.normalize_stem("13 - Lower limb orthoses.md"),
            module.normalize_stem("Lower_limb_orthoses.md"),
        )
        self.assertEqual(
            module.normalize_stem("Rehabilitation of swallowing disorders.pdf 的副本.md"),
            module.normalize_stem("Rehabilitation_of_swallowing_disorders.md"),
        )
        self.assertEqual(
            module.normalize_stem("Source Name (1).md"),
            module.normalize_stem("Source_Name.md"),
        )
        self.assertEqual(
            module.normalize_stem("Achilles tendinopathy - UpToDate.md"),
            module.normalize_stem("Achilles_tendinopathy.md"),
        )
        self.assertEqual(
            module.normalize_raw_reference(
                r"C:\原始資料\opaque\00140130412331290899.md",
                Path(r"C:\原始資料"),
            ),
            "opaque/00140130412331290899.md",
        )
        self.assertEqual(
            module.normalize_raw_reference(
                r"原始資料\opaque\00140130412331290899.md",
                Path(r"C:\原始資料"),
            ),
            "opaque/00140130412331290899.md",
        )

    def test_explicit_raw_source_path_removes_opaque_backlog_entries(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as wiki_dir, tempfile.TemporaryDirectory() as raw_dir:
            wiki = Path(wiki_dir)
            raw = Path(raw_dir) / "原始資料"
            raw.mkdir(parents=True, exist_ok=True)

            for folder in [
                "08_工具與Workflow",
                "09_來源摘要",
            ]:
                (wiki / folder).mkdir(parents=True, exist_ok=True)

            write(wiki / "index.md", "# index\n")
            write(wiki / "SCHEMA.md", "# schema\n")
            write(wiki / "log.md", "# log\n")

            raw_file = raw / "opaque" / "00140130412331290899.md"
            write(raw_file, "raw content\n")
            write(
                wiki / "09_來源摘要/opaque_summary.md",
                f"""
                ---
                title: opaque summary
                created: 2026-04-24
                updated: 2026-04-24
                type: source_summary
                domain: [CPET]
                tags: [summary]
                source_tier: 3
                evidence_level: limited
                confidence: moderate
                contested: false
                contradictions: []
                ---

                - 原始檔：`原始資料/opaque/00140130412331290899.md`
                [[09_來源摘要/opaque_summary]]
                """,
            )

            report = module.analyze_wiki(wiki, raw)
            raw_backlog_paths = {item["path"] for item in report["raw_backlog"]}
            self.assertNotIn("opaque/00140130412331290899.md", raw_backlog_paths)

    def test_contradiction_scan_ignores_workflow_pages_and_generic_limitation_headings(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as wiki_dir, tempfile.TemporaryDirectory() as raw_dir:
            wiki = Path(wiki_dir)
            raw = Path(raw_dir)

            for folder in [
                "08_工具與Workflow",
                "04_CPET",
                "09_來源摘要",
            ]:
                (wiki / folder).mkdir(parents=True, exist_ok=True)

            write(wiki / "index.md", "# index\n")
            write(wiki / "SCHEMA.md", "# schema\n")
            write(wiki / "log.md", "# log\n")

            write(
                wiki / "08_工具與Workflow/flow.md",
                """
                ---
                title: flow
                created: 2026-04-23
                updated: 2026-04-23
                type: workflow
                domain: [methodology]
                tags: [workflow]
                sources: []
                source_tier: 1
                evidence_level: consensus
                confidence: high
                contested: false
                contradictions: []
                ---

                任何衝突都要顯式標示，不可默默覆寫既有結論。
                """,
            )
            write(
                wiki / "04_CPET/method.md",
                """
                ---
                title: method
                created: 2026-04-23
                updated: 2026-04-23
                type: method
                domain: [CPET]
                tags: [method]
                sources: []
                source_tier: 1
                evidence_level: consensus
                confidence: high
                contested: false
                contradictions: []
                ---

                ## 限制 / 爭議
                - 不可把某 breakpoint 誤當成 true boundary。
                """,
            )
            write(
                wiki / "09_來源摘要/real_conflict.md",
                """
                ---
                title: real conflict
                created: 2026-04-23
                updated: 2026-04-23
                type: source_summary
                domain: [CPET]
                tags: [summary]
                source_tier: 1
                evidence_level: consensus
                confidence: high
                contested: false
                contradictions: []
                ---

                本領域目前仍有爭議，存在 conflicting findings。
                """,
            )

            report = module.analyze_wiki(wiki, raw)
            paths = {item["path"] for item in report["contradiction_candidates"]}
            self.assertNotIn("08_工具與Workflow/flow.md", paths)
            self.assertNotIn("04_CPET/method.md", paths)
            self.assertIn("09_來源摘要/real_conflict.md", paths)

    def test_caps_raw_verification_queue_at_five_by_priority(self):
        module = load_module()
        candidates = [
            {"id": "tier3", "tier": 3, "impact": 1, "kind": "backlog"},
            {"id": "tier1-low", "tier": 1, "impact": 2, "kind": "stale"},
            {"id": "tier2", "tier": 2, "impact": 5, "kind": "backlog"},
            {"id": "tier1-high", "tier": 1, "impact": 10, "kind": "contradiction"},
            {"id": "tier1-mid", "tier": 1, "impact": 6, "kind": "missing_core"},
            {"id": "tier1-another", "tier": 1, "impact": 4, "kind": "stale"},
            {"id": "tier3-high", "tier": 3, "impact": 9, "kind": "contradiction"},
        ]

        queue = module.select_raw_verification_queue(candidates, limit=5)

        self.assertEqual(len(queue), 5)
        self.assertEqual(
            [item["id"] for item in queue],
            ["tier1-high", "tier1-mid", "tier1-another", "tier1-low", "tier2"],
        )


if __name__ == "__main__":
    unittest.main()
