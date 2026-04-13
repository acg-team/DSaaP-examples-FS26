from helpers import report_performance


def append_to_list(l: list[float], elements: int):
    for i in range(elements):
        l.append(float(i))
# 100000000 list: 8.971843504905701 seconds


def set_in_preallocated_list(l: list[float], elements: int):
    for i in range(elements):
        l[i] = float(i)
# 100000000 list: 4.398405694961548 seconds


def compare_allocations():
    size = 100000000
    runs = 10
    print(f"Comparing allocations for a {size} list over {runs} runs")
    l = []
    report_performance(runs, append_to_list, l, size)
    l = [0.0] * size
    report_performance(runs, set_in_preallocated_list, l, size)


if __name__ == "__main__":
    compare_allocations()