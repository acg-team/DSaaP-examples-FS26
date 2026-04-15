import time

def time_function(func, *args):
    """
    Times the execution of a given function with the provided arguments.

    Parameters:
    func (callable): The function to be timed.
    *args: Arguments to be passed to the function.

    Returns:
    float: The time taken to execute the function in seconds.
    """
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

def report_performance(runs, func, *args):
    """
    Reports the average execution time of a given function over a specified number of runs.
    Parameters:
    runs (int): The number of times to execute the function for averaging.
    func (callable): The function to be timed.
    *args: Arguments to be passed to the function.

    Returns:
    float: The average time taken to execute the function in seconds.
    """
    times = []
    for _ in range(runs):
        one_run_time = time_function(func, *args)
        times.append(one_run_time)
    average_time = sum(times) / len(times)
    print(f"Execution time ({func.__name__}):\n\t{average_time} seconds")