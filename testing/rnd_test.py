import os
import sys
import unittest
import random

# Make project root importable when running this test directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.rnd import RND
from core.page import Page


class TestRND(unittest.TestCase):
    def make_pages(self):
        pages = []
        for i in range(10):
            p = Page(page_id=i, ptr=0, pid=1)
            p.loaded_time = i
            p.last_access_time = i
            pages.append(p)
        return pages

    def test_random_picks_page_from_list(self):
        """Ensure the random algorithm returns an element from the provided list."""
        pages = self.make_pages()
        algo = RND()
        victim = algo.select_victim_page(pages)

        # The returned victim should be one of the page objects in the list
        self.assertIn(victim, pages)


if __name__ == "__main__":
    unittest.main()
