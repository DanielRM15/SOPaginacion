import re

class OperationParser:
    def __init__(self):
        self.operations = []

    def parse_file(self, file_path):
        operations = []

        try:
            with open(file_path, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        operation = self.parse_line(line)
                        operations.append(operation)
                    except ValueError as e:
                        raise ValueError(f"Error en línea {line_num}: {e}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
        except Exception as e:
            raise Exception(f"Error al leer archivo: {e}")

        return operations
    
    def parse_line(self, line):
        new_match = re.match(r'new\((\d+),(\d+)\)', line)
        if new_match:
            return {
                'type': 'new',
                'pid': int(new_match.group(1)),
                'size': int(new_match.group(2))
            }
        
        use_match = re.match(r'use\((\d+)\)', line)
        if use_match:
            return {
                'type': 'use', 
                'ptr': int(use_match.group(1))
            }
        
        delete_match = re.match(r'delete\((\d+)\)', line)
        if delete_match:
            return {
                'type': 'delete',
                'ptr': int(delete_match.group(1))
            }
        
        kill_match = re.match(r'kill\((\d+)\)', line)
        if kill_match:
            return {
                'type': 'kill',
                'pid': int(kill_match.group(1))
            }
        
        raise ValueError(f"Invalid operation: {line}")
