from core.mmu import MMU
from algorithms.opt import OPT
from algorithms.fifo import FIFO
from algorithms.second_chance import SecondChance
from algorithms.mru import MRU
from algorithms.rnd import RND

class SimulationEngine:
    def __init__(self, operations, algorithm_name, seed=None):

        self.operations = operations
        self.current_operation_index = 0
        self.is_running = False
        self.is_finished = False
        
        #OPT
        opt_algorithm = OPT(operations, {})
        self.mmu_opt = MMU(opt_algorithm)
        
        opt_algorithm.ptr_to_pages = self.mmu_opt.ptr_to_pages
        
        #Other
        selected_algorithm = self._create_algorithm(algorithm_name, seed)
        self.mmu_selected = MMU(selected_algorithm)
        
        self.active_processes = set()
    
    def _create_algorithm(self, algorithm_name, seed):
        if algorithm_name == "FIFO":
            return FIFO()
        if algorithm_name == "SC":
            return SecondChance()
        if algorithm_name == "MRU":
            return MRU()
        if algorithm_name == "RND":
            return RND()
        else:
            raise ValueError(f"Algoritmo desconocido: {algorithm_name}")
    
    def step(self):
        if self.is_finished or self.current_operation_index >= len(self.operations):
            self.is_finished = True
            return False
        
        operation = self.operations[self.current_operation_index]
        
        #Ejecutar en ambas MMUs
        self._execute_operation(self.mmu_opt, operation)
        self._execute_operation(self.mmu_selected, operation)
        
        # Avanzar index de algoritmos
        self.mmu_opt.algorithm.advance()
        self.mmu_selected.algorithm.advance()
        
        self.current_operation_index += 1
        
        return True
    
    def _execute_operation(self, mmu, operation):
        op_type = operation['type']
        
        if op_type == 'new':
            pid = operation['pid']
            size = operation['size']
            ptr = mmu.new(pid, size)
            self.active_processes.add(pid)
            
        elif op_type == 'use':
            ptr = operation['ptr']
            mmu.use(ptr)
            
        elif op_type == 'delete':
            ptr = operation['ptr']
            mmu.delete(ptr)
            
        elif op_type == 'kill':
            pid = operation['pid']
            mmu.kill(pid)
            if pid in self.active_processes:
                self.active_processes.discard(pid)
    
    def run_all(self):
        while not self.is_finished:
            self.step()
    
    def get_statistics(self):
        return {
            'opt': self._get_mmu_stats(self.mmu_opt),
            'selected': self._get_mmu_stats(self.mmu_selected),
            'opt_pages': self._get_pages_info(self.mmu_opt),
            'selected_pages': self._get_pages_info(self.mmu_selected),
            'active_processes': len(self.active_processes),
            'current_operation': self.current_operation_index,
            'total_operations': len(self.operations)
        }
    
    def _get_mmu_stats(self, mmu):
        loaded_pages = sum(1 for p in mmu.physical_memory if p is not None)
        unloaded_pages = len(mmu.virtual_memory)
        
        ram_used_kb = loaded_pages * (mmu.PAGE_SIZE / 1024)
        ram_percent = (loaded_pages / mmu.PHYSICAL_MEMORY_SIZE) * 100
        
        vram_used_kb = unloaded_pages * (mmu.PAGE_SIZE / 1024)
        total_ram_kb = mmu.PHYSICAL_MEMORY_SIZE * (mmu.PAGE_SIZE / 1024)
        vram_percent = (vram_used_kb / total_ram_kb) * 100 if total_ram_kb > 0 else 0
        
        thrashing_time = mmu.page_faults * 5
        thrashing_percent = (thrashing_time / mmu.clock * 100) if mmu.clock > 0 else 0
        
        # ARREGLAR
        fragmentation_kb = self._calculate_fragmentation(mmu)
        
        return {
            'clock': mmu.clock,
            'page_faults': mmu.page_faults,
            'page_hits': mmu.page_hits,
            'ram_used_kb': ram_used_kb,
            'ram_percent': ram_percent,
            'vram_used_kb': vram_used_kb,
            'vram_percent': vram_percent,
            'loaded_pages': loaded_pages,
            'unloaded_pages': unloaded_pages,
            'thrashing_time': thrashing_time,
            'thrashing_percent': thrashing_percent,
            'fragmentation_kb': fragmentation_kb
        }
    
    def _calculate_fragmentation(self, mmu):

        #Hay que calcular fragmentacion en KB, por lo que tenemos que ver como
        #hacemos para obtener la cantidad de memoria desperdiciada despues de un new
        
        return 0
    
    def _get_pages_info(self, mmu):
        pages_info = []
        
        for page_id, page in mmu.page_map.items():
            logical_addr = page_id
            
            physical_addr = page.physical_address if page.is_in_memory else None
            
            disk_addr = None
            if not page.is_in_memory and page in mmu.virtual_memory:
                disk_addr = mmu.virtual_memory.index(page)
            
            loaded_time = page.loaded_time if page.loaded_time is not None else 0
            
            mark = 'X' if page.reference_bit else ''
            
            pages_info.append({
                'page_id': page.page_id,
                'pid': page.pid,
                'ptr': page.ptr,
                'loaded': 'X' if page.is_in_memory else '',
                'logical_addr': logical_addr,
                'physical_addr': physical_addr,
                'disk_addr': disk_addr,
                'loaded_time': loaded_time,
                'mark': mark
            })
        
        pages_info.sort(key=lambda p: p['page_id'])
        
        return pages_info
    
    def pause(self):
        self.is_running = False
    
    def resume(self):
        self.is_running = True
    
    def reset(self):
        self.__init__(self.operations, self.mmu_selected.algorithm.name)
