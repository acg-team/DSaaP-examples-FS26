import subprocess
import numpy as np


def divide_by_two_numpy(matrix: np.ndarray):
    """
    Divides each element of the given matrix by 2 in place using numpy
    """
    matrix /= 2.0


def use_numpy():
    print(f"Dividing a matrix by 2 using numpy version {np.__version__}.")
    size = 5000
    divide_by_two_numpy(
        np.array([[float(i) for i in range(1, size)] for _ in range(size)])
    )
    print("Done.")


def use_blastn():
    cmd = ["blastn", "-version"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout.splitlines()[0])
    except FileNotFoundError:
        print("ERROR: blastn is not installed on this system")
    except subprocess.CalledProcessError as e:
        print("blastn failed:", e)

    print("Done.")


if __name__ == "__main__":
    use_numpy()
    use_blastn()
