from timeit import default_timer
from re import match
from pathlib import Path
from importlib import import_module

if __name__ == "__main__":
    directory = Path(".")

    for file_path in sorted(directory.glob("*.py")):
        if not match(r"\d{2}", file_path.stem):
            continue

        module = import_module(str(file_path.stem))

        start_time = default_timer()
        result = module.solution()
        end_time = default_timer()

        print(f"Problem {file_path.stem}: "
              f"result = {result} "
              f"({(end_time - start_time) * 1000:.3f}ms)")
