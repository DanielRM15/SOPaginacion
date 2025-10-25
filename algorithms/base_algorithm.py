from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def select_victim_page(self, physical_memory):
        pass