from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContract(unittest.TestCase):
    def test_public_vertical_slice_is_complete(self):
        required = [
            ROOT / "README.md",
            ROOT / "BENCHMARK.md",
            ROOT / "CHANGELOG.md",
            ROOT / "assets/readme-banner.png",
            ROOT / "LICENSE",
            ROOT / ".github/workflows/test.yml",
            ROOT / "skills/rules-audit/SKILL.md",
            ROOT / "skills/rules-audit/agents/openai.yaml",
            ROOT / "skills/playtest-planner/SKILL.md",
            ROOT / "skills/playtest-planner/agents/openai.yaml",
            ROOT / "examples/lantern-line/rulebook.md",
            ROOT / "examples/lantern-line/audit.md",
            ROOT / "examples/lantern-line/revised-rulebook.md",
            ROOT / "examples/lantern-line/playtest-plan.md",
        ]
        self.assertTrue(all(path.is_file() for path in required))

    def test_skill_has_no_scaffold_placeholders(self):
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            with self.subTest(skill=path.parent.name):
                skill = path.read_text(encoding="utf-8")
                self.assertIn(f"name: {path.parent.name}", skill)
                self.assertNotIn("TODO", skill)

    def test_example_audit_is_traceable(self):
        audit = (ROOT / "examples/lantern-line/audit.md").read_text(encoding="utf-8")
        self.assertIn("RA-001", audit)
        self.assertEqual(audit.count("**Source:**"), 4)
        self.assertIn("NOT READY FOR BLIND PLAYTEST", audit)

    def test_playtest_plan_is_traceable(self):
        plan = (ROOT / "examples/lantern-line/playtest-plan.md").read_text(encoding="utf-8")
        self.assertIn("PLAN READY", plan)
        self.assertEqual(plan.count("### PT-"), 7)
        self.assertEqual(plan.count("**Cannot establish:**"), 7)

    def test_repository_contains_no_source_documents(self):
        forbidden = {".doc", ".docx", ".odt", ".pdf"}
        found = [path for path in ROOT.rglob("*") if path.suffix.lower() in forbidden]
        self.assertEqual(found, [])


if __name__ == "__main__":
    unittest.main()
