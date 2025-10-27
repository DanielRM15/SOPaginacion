import random

class OperationGenerator:
    def __init__(self):
        self.pointers = []
        self.operations = []

    def generate_operations(self, num_processes, num_operations, seed=None):
        random.seed(seed)
        ptr_counter = 1
        # Generar operaciones 'new' iniciales (uno para cada proceso)
        for i in range(1, num_processes + 1):
            operation = {}
            operation['type'] = 'new'
            operation['pid'] = i
            operation['size'] = random.randint(100, 20000)
            l = [ptr_counter]
            self.pointers.append(l)
            ptr_counter += 1
            self.operations.append(operation)

        # Generar operaciones aleatorias (use, new, delete)
        for i in range(num_processes + 1, num_operations - num_processes + 1):
            operation = {}
            op_type = random.choices(
                ['use', 'new', 'delete'],
                weights=[0.7, 0.2, 0.1],
                k=1
            )[0]
            operation['type'] = op_type

            if op_type == 'use':
                non_empty = [pl for pl in self.pointers if pl]
                if not non_empty:
                    continue
                ptr_list = random.choice(non_empty)
                operation['ptr'] = random.choice(ptr_list)

            elif op_type == 'new':
                pid = random.randint(1, num_processes)
                operation['pid'] = pid
                operation['size'] = random.randint(100, 20000)
                self.pointers[pid-1].append(ptr_counter)
                ptr_counter += 1

            elif op_type == 'delete':
                non_empty = [pl for pl in self.pointers if pl]
                if not non_empty:
                    continue
                ptr_list = random.choice(non_empty)
                operation['ptr'] = random.choice(ptr_list)
                ptr_list.remove(operation['ptr'])

            self.operations.append(operation)

        # Generer operaciones kill
        for i in range(1, num_processes + 1):
            operation = {}
            operation['type'] = 'kill'
            operation['pid'] = i
            self.operations.append(operation)

        return self.operations