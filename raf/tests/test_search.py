import unittest

from raf.models import Link
from raf.search import matches, parse_query, run, score


class QueryTests(unittest.TestCase):
    def test_a_bare_word_is_a_word(self):
        query = parse_query("sqlite")
        self.assertEqual(query.words, ["sqlite"])
        self.assertEqual(query.tags, [])
        self.assertIsNone(query.read)

    def test_tag_and_is_filters_are_understood(self):
        query = parse_query("tag:reading is:unread notes")
        self.assertEqual(query.tags, ["reading"])
        self.assertIs(query.read, False)
        self.assertEqual(query.words, ["notes"])

    def test_an_unknown_filter_is_treated_as_a_word(self):
        self.assertEqual(parse_query("is:somewhere").words, ["is:somewhere"])
        self.assertEqual(parse_query("tag:").tags, [])

    def test_an_empty_query_is_false(self):
        self.assertFalse(parse_query("   "))


class MatchTests(unittest.TestCase):
    def setUp(self):
        self.link = Link(
            url="https://example.com/sqlite-notes",
            title="SQLite notes",
            tags=("reading", "db"),
            note="the pragma page",
            read=False,
        )

    def test_a_word_can_hit_any_field(self):
        for text in ("sqlite", "notes", "pragma", "reading", "example.com"):
            with self.subTest(text=text):
                self.assertTrue(matches(self.link, parse_query(text)))

    def test_a_word_that_is_nowhere_matches_nothing(self):
        self.assertFalse(matches(self.link, parse_query("kubernetes")))

    def test_the_read_filter_reads_the_flag(self):
        self.assertTrue(matches(self.link, parse_query("is:unread")))
        self.assertFalse(matches(self.link, parse_query("is:read")))

    def test_filters_are_and_not_or(self):
        self.assertTrue(matches(self.link, parse_query("tag:db sqlite")))
        self.assertFalse(matches(self.link, parse_query("tag:db kubernetes")))


class RankingTests(unittest.TestCase):
    def setUp(self):
        self.title_hit = Link(url="https://a.test", title="sqlite")
        self.note_hit = Link(url="https://b.test", title="something else", note="sqlite")

    def test_a_title_hit_beats_a_note_hit(self):
        self.assertGreater(score(self.title_hit, parse_query("sqlite")), score(self.note_hit, parse_query("sqlite")))

    def test_a_tag_hit_beats_a_url_hit(self):
        tagged = Link(url="https://c.test", tags=("sqlite",))
        url = Link(url="https://sqlite.test")
        self.assertGreater(score(tagged, parse_query("sqlite")), score(url, parse_query("sqlite")))

    def test_more_words_that_hit_is_a_better_score(self):
        query = parse_query("sqlite notes")
        link = Link(url="https://a.test", title="sqlite notes")
        self.assertGreater(score(link, query), score(self.title_hit, query))

    def test_a_filter_only_query_keeps_everything_it_matches(self):
        links = [self.title_hit, self.note_hit]
        self.assertEqual(len(run(links, "is:unread")), 2)

    def test_the_order_is_by_score_and_then_stable(self):
        links = [self.note_hit, self.title_hit]
        self.assertEqual([link.url for _, link in run(links, "sqlite")][0], "https://a.test")

    def test_nothing_matches_nothing(self):
        self.assertEqual(run([self.title_hit], "kubernetes"), [])


if __name__ == "__main__":
    unittest.main()
