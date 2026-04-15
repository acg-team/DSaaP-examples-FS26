# Python Profiling Example

This directory contains an example to illustrate Python profiling and visualising performance bottlenecks using flame graphs.

## Overview

The profiling example consists of two simple Python scripts.

The first script (`profiling_examply.py`) performs matrix operations with intentional performance characteristics:

- **`do_math_row_column()`**: Applies the `do_silly_stuff()` function to the first element of each row and the `do_math()` function to each element of a 10'000 × 10'000 matrix, iterating row-by-row and column-by-column.
- **`do_silly_stuff()`**: Simulates a time-consuming operation by sleeping for 0.0001 seconds, followed by mathematical operations (squaring, sine, and cosine) on the given value.
- **`do_math()`**: Performs some math including taking the logarithm on the given value.

The second script (`profiling_examply_without_sleep.py`) performs the exact same operations minus the call to the sleep function in `do_silly_stuff()`.

In both cases, the code calls `do_silly_stuff()` N=10'000 times, and `do_math()` N^2 times.

This example is intended to show:
- How to profile Python code using `cProfile`;
- How to convert profiling data into flame graph format using `flameprof`;
- How to visualise performance bottlenecks with the FlameGraph tool.

You can create flame graphs for both versions of the code (`profiling_example.py` and `profiling_example_without_sleep.py`) to see how "optimising" the linear part of the computation affects overall performance.

## Setup

### Prerequisites

- Python 3.6+ with pip;
- Perl (for FlameGraph visualisation).

### Installation

1. **Clone the FlameGraph repository** (if not already present on your machine):
   ```bash
   git clone --depth=1 https://github.com/brendangregg/FlameGraph
   ```

2. **Create and activate a Python virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running

1. **Activate the Python virtual environment** (if not already activated):
   ```bash
   source .venv/bin/activate
   ```

2. **Run profiling**:
   Generate profiler output using Python's built-in `cProfile`:
   ```bash
   python -m cProfile -o o.prof profiling_example.py
   ```

3. **Convert to folded format** (using `flameprof`):
   Convert the profiling output to a format compatible with FlameGraph:
   ```bash
   flameprof o.prof --format log > o.folded
   ```

4. **Generate flame graph** (using the `FlameGraph` Perl tool):
   Create an interactive SVG visualization:
   ```bash
   path/to/FlameGraph/flamegraph.pl o.folded > flamegraph.svg
   ```

You can open the resulting `flamegraph.svg` in a web browser to interactively explore the call stack and execution time distribution.

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP) course, Spring semester 2026 (FS26).

## License

This project is licensed under the MIT License – see the LICENSE file for details.