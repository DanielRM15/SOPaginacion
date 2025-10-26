from .base_algorithm import BaseAlgorithm
import random


class RND(BaseAlgorithm):
    def __init__(self):
        super().__init__("RND")
        self.random_generator = random

    def select_victim_page(self, physical_memory):
        random_victim = self.random_generator.choice(physical_memory)
        return random_victim