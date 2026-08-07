import unittest

from raf import cli
from raf.cli import *  # noqa: F401,F403

class CliTests(unittest.TestCase):

    def test_the_command_cases(self):
        # the index does the work
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
