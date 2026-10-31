"""Current curriculum task 2; only its four retained exercises."""
import sys
from grade_python_basics import main

if __name__ == "__main__":
    sys.argv += ["--task-name", "task02", "--problems", 'coke', 'twttr', 'plates', 'nutrition']
    raise SystemExit(main())
