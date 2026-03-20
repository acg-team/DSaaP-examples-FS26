# Unit Testing Edge Cases

This directory contains an example of unit testing edge cases for a simple discount calculation function using `pytest`.

## Overview

The `discount_test.py` script defines a function `discounted_price(price, percentage)` and a suite of tests that cover:

1.  **Basic Functionality**: Standard positive inputs.
2.  **Floating Point Precision**: Handling float inputs for price and discount.
3.  **Edge Cases**:
    *   Price is zero;
    *   Price is negative.
    *   Discount is 0%.
    *   Discount is > 100%.
    *   Discount is negative.
4.  **Invalid Inputs**:
    *   Price/discount is non-numeric.
    *   Price/discount is numeric, but of the wrong type.

## Setup

To run these examples, you need Python 3 installed. It is recommended to use a virtual environment.

```zsh
# Create and activate virtual environment
python3 -m venv test_venv
source test_venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Tests

Run the tests using `pytest`:

```zsh
pytest discount_test.py
```

## Authors

Jūlija Pečerska, Applied Computational Genomics Team.

Developing Software as a Product (DSaaP) course, Spring semester 2026 (FS26).

## License

This project is licensed under the MIT License – see the LICENSE file for details.