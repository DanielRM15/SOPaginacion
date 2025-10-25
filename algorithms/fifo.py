from .base_algorithm import BaseAlgorithm

class FIFO(BaseAlgorithm):
    def __init__(self):
        super().__init__("FIFO")

    def select_victim_page(self, physical_memory):
        oldest_page = None
        oldest_time = None
        
        for page in physical_memory:
            if page is not None:
                # Buscar la página con el loaded_time más antiguo (menor)
                if oldest_time is None or page.loaded_time < oldest_time:
                    oldest_time = page.loaded_time
                    oldest_page = page
        
        return oldest_page