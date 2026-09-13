from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContract(unittest.TestCase):
    def test_public_vertical_slice_is_complete(self):
        required = [
            ROOT / "README.md",
            ROOT / "LICENSE",
            ROOT / ".github/workflows/test.yml",
            ROOT / "skills/rules-audit/SKILL.md",
            ROOT / "skills/rules-audit/agents/openai.yaml",
            ROOT / "examples/lantern-line/rulebook.md",
            ROOT / "examples/lantern-line/audit.md",
        ]
        self.assertTrue(all(path.is_file() for path in required))

    def test_skill_has_no_scaffold_placeholders(self):
        skill = (ROOT / "skills/rules-audit/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: rules-audit", skill)
        self.assertNotIn("TODO", skill)

    def test_example_audit_is_traceable(self):
        audit = (ROOT / "examples/lantern-line/audit.md").read_text(encoding="utf-8")
        self.assertIn("RA-001", audit)
        self.assertEqual(audit.count("**Source:**"), 5)
        self.assertIn("NOT READY FOR BLIND PLAYTEST", audit)

    def test_repository_contains_no_source_documents(self):
        forbidden = {".doc", ".docx", ".odt", ".pdf"}
        found = [path for path in ROOT.rglob("*") if path.suffix.lower() in forbidden]
        self.assertEqual(found, [])


if __name__ == "__main__":
    unittest.main()
