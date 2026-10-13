import io
import os
import tempfile
import unittest

from raf.cli import main


class CliTests(unittest.TestCase):
    def setUp(self):
        handle, self.path = tempfile.mkstemp(suffix=".db")
        os.close(handle)
        os.unlink(self.path)

    def tearDown(self):
        if os.path.exists(self.path):
            os.unlink(self.path)

    def raf(self, *args):
        out = io.StringIO()
        code = main(["--db", self.path, *args], out=out)
        return code, out.getvalue()

    def test_add_then_list(self):
        code, out = self.raf("add", "example.com/a", "--title", "A", "--tag", "reading")
        self.assertEqual(code, 0)
        self.assertIn("A", out)
        code, out = self.raf("list")
        self.assertEqual(code, 0)
        self.assertIn("A [reading]", out)
        self.assertIn("1 link(s)", out)

    def test_a_bad_url_is_a_message_and_an_exit_code(self):
        code, out = self.raf("add", "mailto:someone@example.com")
        self.assertEqual(code, 1)
        self.assertIn("unsupported scheme", out)

    def test_show_read_and_search(self):
        self.raf("add", "example.com/sqlite", "--title", "SQLite notes", "--note", "the pragma page")
        link_id = self.raf("list")[1].split()[0]
        code, out = self.raf("show", link_id)
        self.assertEqual(code, 0)
        self.assertIn("the pragma page", out)
        self.assertEqual(self.raf("read", link_id)[0], 0)
        self.assertEqual(self.raf("search", "pragma")[1].count("SQLite notes"), 1)

    def test_marking_a_link_that_is_not_there_says_so(self):
        code, out = self.raf("read", "9999")
        self.assertEqual(code, 1)
        self.assertIn("no link 9999", out)

    def test_tags_and_stats_and_the_unread_list(self):
        self.raf("add", "example.com/a", "--tag", "reading")
        self.raf("add", "example.com/b", "--tag", "reading")
        code, out = self.raf("tags")
        self.assertEqual(code, 0)
        self.assertIn("reading", out)
        code, out = self.raf("unread")
        self.assertEqual(out.count("link(s)"), 1)
        code, out = self.raf("stats")
        self.assertIn("total    2", out)
        self.assertIn("unread   2", out)

    def test_export_and_import_round_trip_through_files(self):
        self.raf("add", "example.com/a", "--title", "A", "--tag", "x")
        with tempfile.TemporaryDirectory() as folder:
            dump = os.path.join(folder, "shelf.json")
            self.raf("export", "--out", dump)
            self.assertTrue(os.path.exists(dump))
            os.unlink(self.path)
            code, out = self.raf("import", dump)
            self.assertEqual(code, 0)
            self.assertIn("1 added, 0 skipped", out)

    def test_importing_a_file_that_is_not_a_shelf_says_so(self):
        with tempfile.TemporaryDirectory() as folder:
            junk = os.path.join(folder, "junk.json")
            with open(junk, "w", encoding="utf-8") as handle:
                handle.write("{}")
            code, out = self.raf("import", junk)
            self.assertEqual(code, 1)
            self.assertIn("no links", out)


    def test_an_invalid_port_is_a_message_not_a_traceback(self):
        code, out = self.raf("add", "https://example.com:bad/a")
        self.assertEqual(code, 1)
        self.assertIn("invalid url", out)
        self.assertIn("0 link(s)", self.raf("list")[1])


if __name__ == "__main__":
    unittest.main()
