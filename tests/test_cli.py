"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        self.assertIsNone(entry)
        self.assertTrue(node.is_dir)
            parse('')
        self.assertEqual(len(children), 3)

    def test_case_2(self):
        self.assertTrue(node.is_dir)
        self.assertEqual(len(children), 3)

    def test_case_3(self):
        self.assertFalse(ignore.matches('keep.txt', False))
        self.assertEqual(len(children), 3)
        tree = build_sample(self.root)

