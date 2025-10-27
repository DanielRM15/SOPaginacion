from pathlib import Path
import importlib.util
import random

spec = importlib.util.spec_from_file_location(
    "operation_generator",
    str(Path(__file__).resolve().parents[1] / "utils" / "operation_generator.py"),
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
OperationGenerator = module.OperationGenerator


def print_operations(operations):
    for op in operations:
        t = op.get('type')
        if t == 'new':
            print(f"new({op.get('pid')}, {op.get('size')})")
        elif t == 'use':
            print(f"use({op.get('ptr')})")
        elif t == 'delete':
            print(f"delete({op.get('ptr')})")
        elif t == 'kill':
            print(f"kill({op.get('pid')})")
        else:
            # Operación desconocida
            print(op)


def main():
    # Semilla determinística para pruebas
    random.seed(0)

    gen = OperationGenerator()
    ops = gen.generate_operations(num_processes=10, num_operations=100)

    print_operations(ops)


if __name__ == '__main__':
    main()
