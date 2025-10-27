class Page:
    def __init__(self, page_id: int, ptr: int, pid: int, used_size: int):
        self.page_id = page_id
        self.ptr = ptr
        self.pid = pid
        self.is_in_memory = False
        self.physical_address = None
        self.used_size = used_size
        
        # Properties for algorithms
        self.loaded_time = None
        self.last_access_time = None
        self.reference_bit = False