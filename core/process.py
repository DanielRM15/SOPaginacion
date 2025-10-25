class Process:
    def __init__(self, pid: int):
        self.pid = pid
        self.symbol_table = {}
        self.is_alive = True
    
    def add_ptr(self, ptr, pages):
        self.symbol_table[ptr] = pages

    def get_pages(self, ptr):
        return self.symbol_table.get(ptr, [])
    
    def remove_ptr(self, ptr):
        if ptr in self.symbol_table:
            pages = self.symbol_table[ptr]
            del self.symbol_table[ptr]
            return pages
        return []
    
    def get_all_pages(self):
        all_pages = []
        for pages_list in self.symbol_table.values():
            all_pages.extend(pages_list)
        return all_pages

    def kill(self):
        self.is_alive = False
        all_pages = self.get_all_pages()
        self.symbol_table = {}
        return all_pages