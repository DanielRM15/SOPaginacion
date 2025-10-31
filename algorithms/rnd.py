from .base_algorithm import BaseAlgorithm
import random


class RND(BaseAlgorithm):
    def __init__(self, seed=None):
        super().__init__("RND")
        self.seed = seed
        self.random_generator = random.Random(seed) if seed is not None else random

    def select_victim_page(self, physical_memory):
        candidates = [p for p in physical_memory if p is not None]
        if not candidates:
            return None
        random_victim = self.random_generator.choice(candidates)
        return random_victim