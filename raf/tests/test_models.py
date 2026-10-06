import unittest

from raf.models import InvalidLink, Link, looks_readable, normalise_url, parse_tags


class NormaliseUrlTests(unittest.TestCase):
    def test_a_bare_host_becomes_https(self):
        self.assertEqual(normalise_url("example.com/a"), "https://example.com/a")

    def test_the_fragment_is_dropped_because_it_is_not_the_document(self):
        self.assertEqual(normalise_url("https://example.com/a#part-2"), "https://example.com/a")

    def test_the_query_stays_because_it_changes_what_you_get(self):
        self.assertEqual(normalise_url("https://example.com/s?q=1"), "https://example.com/s?q=1")

    def test_the_scheme_and_the_host_are_lowercased(self):
        self.assertEqual(normalise_url("HTTPS://Example.COM/A"), "https://example.com/A")

    def test_a_port_survives(self):
        self.assertEqual(normalise_url("http://localhost:8080/x"), "http://localhost:8080/x")

    def test_an_empty_path_becomes_a_slash(self):
        self.assertEqual(normalise_url("https://example.com"), "https://example.com/")

    def test_what_we_refuse(self):
        for url in ("", "   ", "mailto:someone@example.com", "ftp://example.com/x", "https://"):
            with self.subTest(url=url), self.assertRaises(InvalidLink):
                normalise_url(url)


class TagTests(unittest.TestCase):
    def test_tags_are_lowercased_sorted_and_unique(self):
        self.assertEqual(parse_tags("Python, python, READING"), ("python", "reading"))

    def test_commas_and_spaces_both_separate(self):
        self.assertEqual(parse_tags("a,b  c"), ("a", "b", "c"))

    def test_nothing_in_nothing_out(self):
        self.assertEqual(parse_tags(None), ())
        self.assertEqual(parse_tags("  , "), ())


class LinkTests(unittest.TestCase):
    def test_the_host_is_available_for_display(self):
        self.assertEqual(Link(url="https://example.com/a").host, "example.com")

    def test_a_read_link_is_marked_in_its_str(self):
        self.assertTrue(str(Link(url="https://a.test", title="A", read=True)).startswith("x "))

    def test_a_bare_url_is_not_worth_keeping(self):
        self.assertFalse(looks_readable(Link(url="https://a.test")))
        self.assertTrue(looks_readable(Link(url="https://a.test", note="ask about this")))


if __name__ == "__main__":
    unittest.main()
