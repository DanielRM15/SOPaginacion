from .base_algorithm import BaseAlgorithm

class OPT(BaseAlgorithm):
    def __init__(self, operations, ptr_to_pages):
        super().__init__("OPT")
        self.operations = operations
        self.ptr_to_pages = ptr_to_pages
        self.current_index = 0
    
    def select_victim_page(self, physical_memory):

        pages_in_memory = [page for page in physical_memory if page is not None]
        
        if not pages_in_memory:
            return None
        
        page_next_use = {}
        
        for page in pages_in_memory:
            next_use_index = self._find_next_use(page.page_id)
            page_next_use[page.page_id] = next_use_index
        
        victim_page_id = max(page_next_use, key=page_next_use.get)
        
        for page in pages_in_memory:
            if page.page_id == victim_page_id:
                return page
        
        return None
    
    def _find_next_use(self, page_id):

        for i in range(self.current_index, len(self.operations)):
            operation = self.operations[i]
            
            if operation['type'] == 'use':
                ptr = operation['ptr']
                
                if ptr in self.ptr_to_pages:
                    page_ids = self.ptr_to_pages[ptr]
                    if page_id in page_ids:
                        return i
        
        return float('inf')
    
    def advance(self):
        self.current_index += 1
