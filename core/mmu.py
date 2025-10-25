from .page import Page
import math

class MMU:
    def __init__(self, algorithm):

        self.PHYSICAL_MEMORY_SIZE = 100
        self.PAGE_SIZE = 4096
        
        self.physical_memory = [None] * 100
        self.virtual_memory = []
        
        self.page_map = {}
        self.ptr_to_pages = {}
        self.next_page_id = 1
        self.next_ptr = 1
        
        self.algorithm = algorithm
        
        self.clock = 0
        self.page_faults = 0
        self.page_hits = 0

    def calculate_pages_needed(self, size_bytes):
        return math.ceil(size_bytes/self.PAGE_SIZE)
    
    def find_free_physical_slot(self):
        for i in range(len(self.physical_memory)):
            if self.physical_memory[i] == None:
                return i
        return None
    
    def move_page_to_virtual(self, page: Page):
        page.is_in_memory = False
        if page.physical_address is not None:
            self.physical_memory[page.physical_address] = None
        self.virtual_memory.append(page)
        page.physical_address = None
        
    def load_page_to_memory(self, page: Page, slot):
        page.is_in_memory = True
        page.physical_address = slot
        self.physical_memory[slot] = page
        if page in self.virtual_memory:
            self.virtual_memory.remove(page)
        page.loaded_time = self.clock
        page.last_access_time = self.clock 

    def new(self, pid, size):
        pages_needed = self.calculate_pages_needed(size)
        created_pages = []

        ptr = self.next_ptr
        self.next_ptr += 1

        for i in range(pages_needed):
            page = Page(self.next_page_id, ptr, pid)
            self.page_map[self.next_page_id] = page
            created_pages.append(page)
            self.next_page_id += 1

        for page in created_pages:
            slot = self.find_free_physical_slot()
            if slot is not None:
                self.load_page_to_memory(page, slot)
                self.page_hits += 1
                self.clock += 1
            else:
                victim_page = self.algorithm.select_victim_page(self.physical_memory)
                if victim_page is None:
                    raise RuntimeError("No se pudo encontrar una página víctima")
                slot = victim_page.physical_address
                self.move_page_to_virtual(victim_page)
                self.load_page_to_memory(page, slot)
                self.page_faults += 1
                self.clock += 5
            
        self.ptr_to_pages[ptr] = [page.page_id for page in created_pages]
        return ptr

    def use(self, ptr):
        if ptr not in self.ptr_to_pages:
            raise ValueError(f"Invalid pointer: {ptr}")
        
        page_ids = self.ptr_to_pages[ptr]
        
        for page_id in page_ids:
            page = self.page_map[page_id]
            
            if not page.is_in_memory:
                slot = self.find_free_physical_slot()
                
                if slot is None:
                    victim_page = self.algorithm.select_victim_page(self.physical_memory)
                    if victim_page is None:
                        raise RuntimeError("No se pudo encontrar una página víctima")
                    slot = victim_page.physical_address
                    self.move_page_to_virtual(victim_page)
                
                self.load_page_to_memory(page, slot)
                self.page_faults += 1
                self.clock += 5
            else:
                self.page_hits += 1
                self.clock += 1
            
            page.last_access_time = self.clock
            page.reference_bit = True

    def delete(self, ptr):
        if ptr not in self.ptr_to_pages:
            return
        
        page_ids = self.ptr_to_pages[ptr]
        for page_id in page_ids:
            page = self.page_map[page_id]
            if page.is_in_memory:
                self.physical_memory[page.physical_address] = None
            else:
                self.virtual_memory.remove(page)
            del self.page_map[page_id]
        
        del self.ptr_to_pages[ptr]

    def kill(self, pid):
        ptrs_to_delete = []
        for ptr, page_ids in self.ptr_to_pages.items():
            if page_ids and self.page_map[page_ids[0]].pid == pid:
                ptrs_to_delete.append(ptr)
        
        for ptr in ptrs_to_delete:
            self.delete(ptr)
        