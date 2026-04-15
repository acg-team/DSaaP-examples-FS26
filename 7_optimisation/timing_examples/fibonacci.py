from helpers import report_performance

def fibonacci_recursive(n: int) -> int:
    """
    Computes the nth Fibonacci number using a naive recursive approach.
    """
    print(n)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + \
               fibonacci_recursive(n - 2)
# For 40: 13.901220798492432 seconds

def fibonacci_list(n: int) -> int:
    """
    Computes the nth Fibonacci number using a list-based approach.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fibs = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]
# For 40: 3.2186508178710938e-06 seconds


def fibonacci_three_vars(n: int) -> int:
    """
    Computes the nth Fibonacci number using constant space.
    Uses three intermediate variables: prev2, prev1, and curr.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    (prev2, prev1, curr) = (0, 1, 1)
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return curr
# For 40: 1.4543533325195312e-06 seconds


def compare_fibonacci():
    n = 100000
    runs = 10
    print(f"Comparing Fibonacci implementations for n={n} over {runs} runs")
    report_performance(runs, fibonacci_recursive, n)
    report_performance(runs, fibonacci_list, n)
    report_performance(runs, fibonacci_three_vars, n)

if __name__ == "__main__":
    compare_fibonacci()