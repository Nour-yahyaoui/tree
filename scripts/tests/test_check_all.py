"""The workspace runner must finish every suite, even after a failure."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "check-all.sh"
RUNNER = """#!/bin/sh
case "$(basename "$PWD")" in
    treepy) project=treepy; status=${TREEPY_STATUS:-0} ;;
    raf) project=raf; status=${RAF_STATUS:-0} ;;
    masrouf) project=masrouf; status=${MASROUF_STATUS:-0} ;;
    *) project=helpers; status=${HELPERS_STATUS:-0} ;;
esac
printf 'ran %s\\n' "$project"
exit "$status"
"""


class CheckAllTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="tree runner ")
        self.addCleanup(temporary.cleanup)
        self.parent = Path(temporary.name)
        self.root = self.parent / "workspace"
        for directory in ("scripts", "treepy", "raf", "masrouf", "bin"):
            (self.root / directory).mkdir(parents=True)
        self.script = self.root / "scripts" / SCRIPT.name
        shutil.copy2(SCRIPT, self.script)
        for name in ("make", "python3", "npm"):
            stub = self.root / "bin" / name
            stub.write_text(RUNNER)
            stub.chmod(0o755)

    def run_script(self, **statuses):
        env = {**os.environ, "PATH": str(self.root / "bin") + os.pathsep + os.defpath}
        for project in ("HELPERS", "TREEPY", "RAF", "MASROUF"):
            env[project + "_STATUS"] = str(statuses.get(project, 0))
        return subprocess.run(
            ["sh", str(self.script)], cwd=self.parent, env=env,
            text=True, capture_output=True, check=False,
        )

    def assert_every_suite_ran(self, result):
        for project in ("helpers", "treepy", "raf", "masrouf"):
            self.assertIn("ran " + project, result.stdout)

    def test_success_reports_all_suites(self):
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_every_suite_ran(result)
        self.assertIn("all projects passed", result.stdout)

    def test_first_failure_does_not_stop_later_suites(self):
        result = self.run_script(HELPERS=1)
        self.assertEqual(result.returncode, 1)
        self.assert_every_suite_ran(result)
        self.assertIn("failed: helpers", result.stdout)
        self.assertNotIn("all projects passed", result.stdout)

    def test_reports_every_failure_in_order(self):
        result = self.run_script(TREEPY=2, RAF=3, MASROUF=4)
        self.assertEqual(result.returncode, 1)
        self.assert_every_suite_ran(result)
        self.assertIn("failed: treepy raf masrouf", result.stdout)


if __name__ == "__main__":
    unittest.main()
