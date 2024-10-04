from timeit import default_timer
from re import match
from pathlib import Path
from importlib import import_module

if __name__ == "__main__":
    directory = Path(".")

    total_time = 0

    for file_path in sorted(directory.glob("*.py")):
        if not match(r"\d{2}", file_path.stem):
            continue

        module = import_module(str(file_path.stem))

        start_time = default_timer()
        result = module.solution()
        end_time = default_timer()

        time = end_time - start_time
        total_time += time

        print(f"Problem {file_path.stem}: result = {result} ({time * 1000:.3f}ms)")

    print(f"Total time: {total_time:.3f}s")
