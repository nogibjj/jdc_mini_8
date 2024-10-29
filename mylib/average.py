import pandas as pd
import time
import psutil


def average(path):
    nfl_data = pd.read_csv(path)

    try_avg = nfl_data["career_try"].mean()
    return try_avg


def calculate_time_memory(path):
    # Record the start time
    start_time = time.time()

    # Measure the initial memory usage
    process = psutil.Process()  # Get current process
    start_mem_usage = process.memory_info().rss  # Memory usage in bytes

    # Calculate the average
    average(path)

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Measure the final memory usage
    end_mem_usage = process.memory_info().rss  # Memory usage in bytes

    # Convert memory usage from bytes to kilobytes
    memory_usage_change = (end_mem_usage - start_mem_usage) / 1024

    print(f"Python-Elapsed Time: {elapsed_time:.7f} seconds")
    print(f"Python-Memory Usage Change: {memory_usage_change:.2f} kilobytes")

    return end_mem_usage, elapsed_time
