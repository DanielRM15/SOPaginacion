import os
import sys
import unittest

# Make project root importable when running this test directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.mru import MRU
from core.page import Page


class TestMRU(unittest.TestCase):
    def make_pages(self):
        pages = []
        for i in range(10):
            p = Page(page_id=i, ptr=0, pid=1)
            p.loaded_time = i
            p.last_access_time = i
            pages.append(p)
        return pages

    def test_selects_most_recently_used(self):
        """With last_access_time 0..9, MRU should select the page with time 9."""
        pages = self.make_pages()
        algo = MRU()
        victim = algo.select_victim_page(pages)

        self.assertIsNotNone(victim)
        self.assertEqual(victim.last_access_time, 9)
        self.assertIs(victim, pages[9])

    def test_ties_choose_first_max(self):
        """If multiple pages share the max last_access_time, the first encountered should be returned."""
        pages = self.make_pages()
        # set two pages to share the max last_access_time
        pages[8].last_access_time = 15
        pages[2].last_access_time = 15

        algo = MRU()
        victim = algo.select_victim_page(pages)

        self.assertIsNotNone(victim)
        # MRU uses '>' comparison so the first page with the max time seen will be kept
        # pages[2] appears before pages[8], so when scanning from index 0..9, pages[2] will be kept
        self.assertEqual(victim.last_access_time, 15)
        self.assertIs(victim, pages[2])


if __name__ == "__main__":
    unittest.main()
