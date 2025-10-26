from .base_algorithm import BaseAlgorithm

class MRU(BaseAlgorithm):
    def __init__(self):
        super().__init__("MRU")

    def select_victim_page(self, physical_memory):
        mru_page = None
        mru_time = None
        
        for page in physical_memory:
            if page is not None:
                if mru_time is None or page.last_access_time > mru_time:
                    mru_time = page.last_access_time
                    mru_page = page
        
        return mru_page