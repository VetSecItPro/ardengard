"""The workbook build validates its links and regenerates the page and markdown without errors."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class BuildWorkbookTest(unittest.TestCase):
    def run_build(self, mutate=None):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            if mutate:
                mutate(copy)
            result = subprocess.run([sys.executable, "scripts/build_workbook.py"], cwd=copy, capture_output=True, text=True)
            page = (copy / "artifacts" / "agent-wishlist" / "index.html")
            return result, page.read_text() if page.exists() else ""

    def test_build_succeeds_and_writes_page(self):
        result, page = self.run_build()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("<title>Agent Wishlist</title>", page)
        self.assertNotIn("__DATA__", page)

    def test_build_rejects_em_dash(self):
        def add_dash(copy):
            log = copy / "docs" / "discussion-log.md"
            log.write_text(log.read_text() + "\n## test\n\n- bad — dash\n")
        result, _ = self.run_build(add_dash)
        self.assertNotEqual(result.returncode, 0)

    def test_build_rejects_unknown_requirement(self):
        def break_link(copy):
            plan = copy / "docs" / "plan" / "plan.json"
            data = json.loads(plan.read_text())
            data["phases"][0]["tasks"][0]["req"] = ["R999"]
            plan.write_text(json.dumps(data))
        result, _ = self.run_build(break_link)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("R999", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
