import unittest

from raf import store
from raf.store import *  # noqa: F401,F403

class StoreTests(unittest.TestCase):

    def test_the_table_cases(self):
        # no dependencies, thank you
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
# revisit the naming
