from .base_algorithm import BaseAlgorithm

class SecondChance(BaseAlgorithm):
    def __init__(self):
        super().__init__("SecondChance")

    def select_victim_page(self, physical_memory):
        oldest_page = None
        oldest_time = None

        while oldest_page is None or oldest_page.reference_bit:
            sc_loaded_time = -1
            if (oldest_page is not None):
                oldest_page.reference_bit = False
                sc_loaded_time = oldest_page.loaded_time

            oldest_page = None
            oldest_time = None
            for page in physical_memory:
                if page is not None:
                    if (oldest_time is None or page.loaded_time < oldest_time) and page.loaded_time > sc_loaded_time:
                        oldest_time = page.loaded_time
                        oldest_page = page
        
        return oldest_page