import json
import os
from pathlib import Path
import tempfile
from unittest.mock import patch
import unittest

from raf.models import InvalidLink
from raf.store import SCHEMA_VERSION, Shelf


class ShelfTests(unittest.TestCase):
    def setUp(self):
        self.shelf = Shelf(":memory:")

    def tearDown(self):
        self.shelf.close()

    def test_the_schema_records_its_own_version(self):
        version = self.shelf.db.execute("PRAGMA user_version").fetchone()[0]
        self.assertEqual(version, SCHEMA_VERSION)

    def test_a_link_comes_back_with_its_tags(self):
        link = self.shelf.add("https://example.com/a", title="A", tags="reading, later")
        self.assertEqual(link.tags, ("later", "reading"))
        self.assertEqual(self.shelf.get(link.id).title, "A")

    def test_the_same_url_twice_is_the_same_link(self):
        first = self.shelf.add("https://example.com/a", title="A")
        second = self.shelf.add("https://example.com/a", title="A again")
        self.assertEqual(first.id, second.id)
        self.assertEqual(len(self.shelf.links()), 1)
        self.assertEqual(second.title, "A", "the first title wins, nothing is overwritten")

    def test_a_bad_url_is_refused_before_anything_is_written(self):
        with self.assertRaises(InvalidLink):
            self.shelf.add("mailto:someone@example.com")
        self.assertEqual(self.shelf.links(), [])

    def test_tags_can_be_added_and_removed(self):
        link = self.shelf.add("https://example.com/a")
        self.assertEqual(self.shelf.tag(link.id, "one two"), 2)
        self.assertEqual(self.shelf.tag(link.id, "one"), 0, "the same tag twice is not an error")
        self.assertEqual(self.shelf.untag(link.id, "one"), 1)
        self.assertEqual(self.shelf.get(link.id).tags, ("two",))

    def test_marking_answers_whether_the_link_is_there_in_that_state(self):
        link = self.shelf.add("https://example.com/a")
        self.assertTrue(self.shelf.mark(link.id))
        self.assertTrue(self.shelf.get(link.id).read)
        self.assertTrue(self.shelf.mark(link.id), "marking an already read link is not an error")
        self.assertTrue(self.shelf.mark(link.id, read=False))
        self.assertFalse(self.shelf.get(link.id).read)
        self.assertFalse(self.shelf.mark(9999), "a link that is not there cannot be marked")

    def test_removing_a_link_takes_its_tags_with_it(self):
        link = self.shelf.add("https://example.com/a", tags="x")
        self.assertTrue(self.shelf.remove(link.id))
        self.assertFalse(self.shelf.remove(link.id))
        self.assertEqual(self.shelf.db.execute("SELECT COUNT(*) FROM tags").fetchone()[0], 0)

    def test_unread_and_the_tag_filter_are_the_same_query_language(self):
        a = self.shelf.add("https://example.com/a", tags="reading")
        b = self.shelf.add("https://example.com/b", tags="reading")
        self.shelf.mark(a.id)
        self.assertEqual([link.id for link in self.shelf.links(unread_only=True)], [b.id])
        self.assertEqual({link.id for link in self.shelf.links(tag="reading")}, {a.id, b.id})

    def test_the_newest_link_is_first(self):
        first = self.shelf.add("https://example.com/1")
        second = self.shelf.add("https://example.com/2")
        self.assertEqual([link.id for link in self.shelf.links()][0], second.id)
        self.assertEqual(self.shelf.links()[-1].id, first.id)

    def test_stats_add_up(self):
        a = self.shelf.add("https://example.com/a", tags="x y")
        self.shelf.add("https://example.com/b")
        self.shelf.mark(a.id)
        self.assertEqual(self.shelf.stats(), {"total": 2, "read": 1, "unread": 1, "tags": 2, "hosts": 1})

    def test_an_export_imports_again(self):
        self.shelf.add("https://example.com/a", title="A", tags="x", note="n")
        self.shelf.add("https://example.com/b")
        payload = self.shelf.export()

        other = Shelf(":memory:")
        added, skipped = other.import_(payload)
        self.assertEqual((added, skipped), (2, 0))
        # every field comes back; the order inside the file may not, because
        # the ids are new (and the date the links were saved is restored)
        self.assertEqual(sorted_links(other.export()), sorted_links(payload))
        other.close()

    def test_an_import_skips_what_it_cannot_read_and_says_so(self):
        payload = '{"version": 2, "links": [{"url": "https://ok.test"}, {"url": "mailto:x@y.z"}, {"nothing": 1}]}'
        added, skipped = self.shelf.import_(payload)
        self.assertEqual((added, skipped), (1, 2))

    def test_a_file_that_is_not_an_export_is_refused(self):
        for text in ("not json", "{}", '{"links": 5}'):
            with self.subTest(text=text), self.assertRaises(InvalidLink):
                self.shelf.import_(text)


    def test_stats_count_hosts_not_urls_or_ports(self):
        self.shelf.add("http://example.com/a")
        self.shelf.add("https://example.com:8080/b")
        self.shelf.add("https://other.test/a")
        self.assertEqual(self.shelf.stats()["hosts"], 2)


class ShelfPathTests(unittest.TestCase):
    def test_home_directory_paths_are_expanded_before_opening(self):
        with tempfile.TemporaryDirectory() as folder:
            home = Path(folder) / "home"
            home.mkdir()
            previous = os.getcwd()
            try:
                os.chdir(folder)  # a broken implementation cannot write into the checkout
                with patch.dict(os.environ, {"HOME": str(home)}):
                    shelf = Shelf("~/.raf/shelf.db")
                try:
                    expected = home / ".raf" / "shelf.db"
                    self.assertEqual(shelf.path, str(expected))
                    self.assertTrue(expected.is_file())
                    self.assertFalse((Path(folder) / "~").exists())
                finally:
                    shelf.close()
            finally:
                os.chdir(previous)


if __name__ == "__main__":
    unittest.main()


def sorted_links(payload: str):
    data = json.loads(payload)
    return sorted(data["links"], key=lambda item: item["url"])
