# Optimisation Examples

This directory contains Python examples for the **Optimisation** lecture.

The examples cover two complementary aspects of performance analysis.

## Structure

```
7_optimisation/
├── timing_examples/     # Benchmark comparisons of different Python implementations
└── profiling_example/   # Python profiling with cProfile and flame graph visualisation
```

### [`timing_examples/`](timing_examples/README.md)

Benchmarks that compare the runtime of different implementations of common operations — including Fibonacci computation, matrix traversal patterns, list allocation strategies, and sorting algorithm behaviour. Demonstrates the impact of algorithmic choices, memory access patterns, and library selection (plain Python vs. NumPy).

### [`profiling_example/`](profiling_example/README.md)

An end-to-end example that shows how to profile a Python application using `cProfile`, convert the output to a folded stack format with `flameprof`, and generate an interactive flame graph SVG with [Brendan Gregg's FlameGraph tool](https://github.com/brendangregg/FlameGraph).

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP) course, Spring semester 2026 (FS26).

## License

This project is licensed under the MIT License – see the LICENSE file for details.
