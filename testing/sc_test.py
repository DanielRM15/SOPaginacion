import os
import sys
import unittest

# Make project root importable when running this test directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.second_chance import SecondChance
from core.page import Page


class TestSecondChance(unittest.TestCase):
	def make_pages(self):
		pages = []
		for i in range(10):
			p = Page(page_id=i, ptr=0, pid=1)
			p.loaded_time = i
			# default reference_bit is False
			pages.append(p)
		return pages

	def test_selects_first_unreferenced_after_referenced_block(self):
		"""Pages 0-4 are referenced; victim should be page with loaded_time 5."""
		pages = self.make_pages()
		for i in range(5):
			pages[i].reference_bit = True

		algo = SecondChance()
		victim = algo.select_victim_page(pages)

		self.assertIsNotNone(victim)
		self.assertEqual(victim.loaded_time, 5)
		self.assertIs(victim, pages[5])

	def test_all_referenced_resets_and_selects_oldest(self):
		"""If all pages are referenced initially, bits get cleared and the oldest page should be selected."""
		pages = self.make_pages()
		for p in pages:
			p.reference_bit = True

		algo = SecondChance()
		victim = algo.select_victim_page(pages)

		self.assertIsNotNone(victim)
		self.assertEqual(victim.loaded_time, 0)
		self.assertIs(victim, pages[0])


if __name__ == "__main__":
	unittest.main()

