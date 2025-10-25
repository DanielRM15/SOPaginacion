class Page:
    def __init__(self, page_id: int, ptr: int, pid: int):
        self.page_id = page_id
        self.ptr = ptr
        self.pid = pid
        self.is_in_memory = False
        self.physical_address = None
        
        # Properties for algorithms
        self.loaded_time = None
        self.last_access_time = None
        self.reference_bit = False