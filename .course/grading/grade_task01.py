"""Current curriculum task 1; only its four retained exercises."""
import sys
from grade_python_basics import main

if __name__ == "__main__":
    sys.argv += ["--task-name", "task01", "--problems", 'faces', 'tip', 'bank', 'meal']
    raise SystemExit(main())
