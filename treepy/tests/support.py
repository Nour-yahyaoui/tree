"""Helpers shared by the test modules.

Every test builds its own tree in a temporary directory and throws it away
afterwards; nothing here touches the repository itself.
"""

from __future__ import annotations

import os
import shutil
import tempfile
import unittest


class TempTreeCase(unittest.TestCase):
    """A TestCase with a scratch directory and a tiny tree builder."""

    def setUp(self) -> None:
        self.root = tempfile.mkdtemp(prefix="treepy-test-")
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)

    def make(self, relative: str, content: str = "") -> str:
        """Create a file (and its parents) under the scratch directory."""
        path = os.path.join(self.root, relative)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)
        return path

    def mkdir(self, relative: str) -> str:
        path = os.path.join(self.root, relative)
        os.makedirs(path, exist_ok=True)
        return path

    def sample(self) -> None:
        """The tree most tests work against.

        ::

            alpha.txt
            sub/
                beta.py
                deep/
                    gamma.md
            .hidden/
                secret.txt
        """
        self.make("alpha.txt", "a")
        self.make("sub/beta.py", "b")
        self.make("sub/deep/gamma.md", "c")
        self.make(".hidden/secret.txt", "d")


def names(node) -> list:
    """Names of a node and all of its descendants, depth first."""
    return [item.name for item in node.walk()]


def relative_names(node) -> list:
    """Relative paths of a node and all of its descendants."""
    return [item.name if not item.relative else item.relative for item in node.walk()]
