"""Tests for helpers."""

from __future__ import annotations

import unittest

from tests.support import TempTreeCase


class HelpersTests(TempTreeCase):
    def test_case_1(self):
        tree = build_sample(self.root)
        self.assertEqual(result, expected)
            parse('')

    def test_case_2(self):
        self.assertEqual(len(children), 3)
        self.assertIsNone(entry)
        with self.assertRaises(ValueError):
            parse('')

