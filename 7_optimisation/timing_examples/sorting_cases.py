from random import randrange
from helpers import report_performance

def bubble_sort(arr: list[int]) -> list[int]:
    comparisons = 0
    swaps = 0
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                swapped = True
                arr[j], arr[j+1] = \
                     arr[j+1], arr[j]
        if not swapped:
            break
    return arr
    # Worst case (reverse-sorted): O(n^2)
    # For 10000: ~7.2 seconds
    # Average case (random): O(n^2)
    # For 10000: ~6.42 seconds
    # Best case (already sorted): O(n)
    # For 10000: ~0.00072 seconds

def compare_sorts():
    size = 10000
    runs = 10
    print(f"Comparing sorting algorithms for a list of size {size} over {runs} runs")

    arr = [randrange(size) for _ in range(size)]
    print("Sorting a random list:")
    report_performance(runs, bubble_sort, arr.copy())

    arr = [size - i for i in range(size)]
    print("Sorting a reverse-sorted list:")
    report_performance(runs, bubble_sort, arr.copy())

    arr = [i for i in range(size)]
    print("Sorting an already sorted list:")
    report_performance(runs, bubble_sort, [i for i in range(size)])

if __name__ == "__main__":
    compare_sorts()