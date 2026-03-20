# Unit Test Pitfalls

This directory demonstrates common anti-patterns in unit testing and how to fix them.

## Pitfalls & Fixes

### 1. Assertion Too Strict ([`assertion_too_strict.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/assertion_too_strict.py))

A common mistake is asserting exact equality for floating point numbers. Hardcoding expected float values with high precision can make tests fail despite the output being correct.

**Fix**: Use `pytest.approx()` to allow for a margin of error. See [`assertion_too_strict_fixed.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/assertion_too_strict_fixed.py).

### 2. Multiple Assertions ([`multiple_values.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/multiple_values.py))

Grouping multiple distinct test cases into a single `test_` function is bad practice. If the first assertion fails, execution stops, and you don't know if subsequent cases pass or fail.

**Fix**: Split each case into its own test function with a descriptive name. See [`multiple_values_fixed.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/multiple_values_fixed.py).

### 3. Implementation Details ([`implementation_details.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/implementation_details.py))

Testing *how* the code works (e.g., spying on specific internal function calls) instead of *what* it does creates brittle tests. If you refactor the internal implementation but keep the same behavior, the test will break.

**Fix**: Test the public API contract (input vs output), not implementation details. See [`implementation_details_fixed.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/implementation_details_fixed.py).

### 4. Environment Dependency ([`environment_dependency.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/environment_dependency.py))

Tests that rely on external environment state (like `datetime.now()`) are flaky. They might pass today but fail tomorrow (e.g., on weekends vs weekdays).

**Fix**: Pass the dependency as a parameter (dependency injection). See [`environment_dependency_fixed.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/environment_dependency_fixed.py).

### 5. Overusing Mocks ([`environment_dependency_fix_with_mock.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/environment_dependency_fix_with_mock.py))

Mocking is a powerful tool to remove external dependencies, but it's easy to overdo. The previous example could be fixed using mocks (see [`environment_dependency_fix_with_mock.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/environment_dependency_fix_with_mock.py)), but is that really necessary? Simple dependency injection is often cleaner and less brittle.

**Fix**: Pass the dependency as a parameter (dependency injection). See [`environment_dependency_fixed.py`](https://github.com/acg-team/DSaaP-examples-FS26/blob/main/5_testing/unit_test_pitfalls/environment_dependency_fixed.py).

## Setup

To run these examples, you need Python 3 installed and a clone of the [DSaaP examples repository]( https://github.com/acg-team/DSaaP-examples-FS26 ).

You can use a virtual environment to install dependencies:

```zsh
# Clone the repository if you haven't already
# git clone git@github.com:acg-team/DSaaP-examples-FS26.git
# cd DSaaP-examples-FS26/5_testing/unit_test_pitfalls

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

Run specific files using pytest:

```zsh
pytest assertion_too_strict.py
# vs
pytest assertion_too_strict_fixed.py
```

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP) course, Spring semester 2026 (FS26).

## License

This project is licensed under the MIT License – see the LICENSE file for details.