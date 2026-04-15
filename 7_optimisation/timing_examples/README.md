# Python Code Timing Examples

This directory contains examples that benchmark different Python implementations of common operations, illustrating the performance impact of algorithmic choices, memory access patterns, and library selection.

## Overview

Each script uses a `report_performance()` helper from `helpers.py` that times a function over multiple runs and prints the average execution time. The following examples are provided, in order of mention in the lecture slides, timed on 2.3 GHz Intel Core i7.

### Matrix traversal and math

`matrix_functions.py` compares matrix traversal and operation strategies on 5'000x5'000 matrices:

- Division of each element by 2:
  - Row-major iteration (`divide_by_two_row_major`): ~1.3 seconds;
  - Column-major iteration (cache locality effects, `divide_by_two_column_major`): ~6.3 seconds;
  - NumPy matrix operations: ~0.017 seconds (>75x faster than pure Python iteration);

- Row-major iteration with simple division of each element vs more complex operations:
  - Simple division (`divide_by_two_row_major`): ~1.3 seconds;
  - 3 math operations, division, sum, logarithm (`do_math_row_major`): ~3.1 seconds;

- Row-major iteration with complex operations using builtin `math.log` vs `numpy.log`:
  - Builtin log (`do_math_row_major`): ~3.1 seconds;
  - NumPy log (`do_numpy_math_row_major`): ~15.4 seconds.


### Time needed for memory allocation

`list_allocations.py` compares dynamic vs. pre-allocated list population for 100M elements:
  - `append_to_list`: appending to an empty list: ~9.0 seconds;
  - `set_in_preallocated_list`: writing into a pre-allocated list: ~4.4 seconds (~2x faster).


### Time and space complexity

`fibonacci.py` compares three implementations of the Fibonacci sequence on N=40:

- `fibonacci_recursive`: naive recursive approach — exponential time complexity, O(N) space due to recursive calls: ~13.9 seconds;
- `fibonacci_list`: list-based dynamic programming — O(N) time, O(N) space, ~3.2 microseconds;
- `fibonacci_three_vars`: iterative constant-space approach — O(N) time, O(1) space, ~1.5 microseconds.


### Worst vs average vs best case runtime

`sorting_cases.py` enchmarks bubble sort on 10,000 elements across best, average, and worst cases:

- Reverse-sorted input (worst case): ~7.2 seconds;
- Random input (average case): ~6.4 seconds;
- Already-sorted input (best case, early exit): ~0.0007 seconds.

## Setup

### Prerequisites

- Python 3.6+ with pip.

### Installation

1. **Create and activate a Python virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running

1. **Activate the Python virtual environment** (if not already activated):
   ```bash
   source .venv/bin/activate
   ```

2. **Run examples**:
   Each script can be run directly. For example:
   ```bash
   python fibonacci.py
   python matrix_functions.py
   python list_allocations.py
   python sorting_cases.py
   ```

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP) course, Spring semester 2026 (FS26).

## License

This project is licensed under the MIT License – see the LICENSE file for details.