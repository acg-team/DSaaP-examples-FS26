# Why We Test

This directory contains a series of examples demonstrating the progression from manual testing to automated unit testing, using a simple discount calculation function.

## Setup

To run these examples, you need Python 3 installed and a clone of the [DSaaP examples repository]( https://github.com/acg-team/DSaaP-examples-FS26 ).

You can use a virtual environment to install dependencies:

```zsh
# Clone the repository if you haven't already
git clone git@github.com:acg-team/DSaaP-examples-FS26.git
cd DSaaP-examples-FS26/5_testing/why_unit_test

# Create and activate virtual environment
python3 -m venv test_venv
source test_venv/bin/activate

# Install dependencies (pytest, pytest-mock)
pip install -r requirements.txt
```

Alternatively, you can install the dependencies system-wide:
```zsh
pip install -r requirements.txt
```

## Running the Examples

### 1. Manual Checks

These scripts rely on manual verification (print statements) to check correctness. Run them directly with Python.

- **Basic Check**: verifying a simple discount calculation.
  ```zsh
  python 0_discount_manual_check.py
  ```

- **Edge Case Check**: verifying behavior with unusual inputs (e.g., >100% discount).
  ```zsh
  python 1_discount_edge_case.py
  ```

- **Bug Introduction**: a script that contains a subtle bug in the logic, which might be missed without proper checks.
  ```zsh
  python 2_discount_introduced_bug.py
  ```

### 2. Automated Testing with pytest

These examples use `pytest` for automated test execution. Run them using the `pytest` command.

- **Basic Tests**: introduces simple unit tests for the discount function.
  ```zsh
  pytest 3_discount_with_tests.py
  ```

- **Edge Case Tests**: expands tests to handle edge cases.
  ```zsh
  pytest 4_discount_with_tests_edge_cases.py
  ```

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP) course, Spring semester 2026 (FS26).

## License

This project is licensed under the MIT License – see the LICENSE file for details.