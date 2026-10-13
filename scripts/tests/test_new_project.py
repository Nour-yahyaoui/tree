"""Exercise the scaffold helper in an isolated workspace, never this checkout."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "new-project.sh"


class NewProjectTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="tree workspace ")
        self.addCleanup(temporary.cleanup)
        self.parent = Path(temporary.name)
        self.root = self.parent / "workspace"
        (self.root / "scripts").mkdir(parents=True)
        self.script = self.root / "scripts" / SCRIPT.name
        shutil.copy2(SCRIPT, self.script)

    def run_script(self, *args):
        return subprocess.run(
            ["sh", str(self.script), *args],
            cwd=self.parent,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_creates_a_readme_and_prints_the_checklist(self):
        result = self.run_script("small_project-2")
        self.assertEqual(result.returncode, 0, result.stderr)
        readme = (self.root / "small_project-2" / "README.md").read_text()
        self.assertTrue(readme.startswith("# small_project-2\n"))
        self.assertIn("true   # replace with the real test command", readme)
        self.assertIn("scripts/check-all.sh", result.stdout)
        self.assertIn(".github/workflows/ci.yml", result.stdout)
        self.assertIn("scripts/list-projects.sh", result.stdout)
        self.assertIn("release", result.stdout)
        self.assertFalse((self.parent / "small_project-2").exists())

    def test_requires_exactly_one_argument(self):
        for args in ((), ("first", "second")):
            with self.subTest(args=args):
                result = self.run_script(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("usage:", result.stderr)
                self.assertFalse((self.root / "first").exists())

    def test_rejects_unsafe_or_non_project_names(self):
        for name in (
            "", "../escaped", "nested/path", ".hidden", "Uppercase", "bad name",
            "-option", "my.project", "école", str(self.parent / "absolute"),
        ):
            with self.subTest(name=name):
                result = self.run_script(name)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual([path.name for path in self.root.iterdir()], ["scripts"])
                self.assertFalse((self.parent / "escaped").exists())
                self.assertFalse((self.parent / "absolute").exists())

    def test_leaves_an_existing_directory_untouched(self):
        project = self.root / "existing"
        project.mkdir()
        readme = project / "README.md"
        readme.write_text("keep this\n")
        result = self.run_script("existing")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("already exists", result.stderr)
        self.assertEqual(readme.read_text(), "keep this\n")

    def test_refuses_an_existing_file(self):
        target = self.root / "existing"
        target.write_text("not a directory\n")
        result = self.run_script("existing")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(target.read_text(), "not a directory\n")

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_refuses_a_dangling_symlink(self):
        target = self.root / "existing"
        target.symlink_to(self.parent / "absent")
        result = self.run_script("existing")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("already exists", result.stderr)
        self.assertTrue(target.is_symlink())
        self.assertFalse((self.parent / "absent").exists())


if __name__ == "__main__":
    unittest.main()
