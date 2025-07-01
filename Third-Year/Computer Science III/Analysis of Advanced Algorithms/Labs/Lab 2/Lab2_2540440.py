import random
import time

# Below is the code I used in lab 1
def random_distinct_integers(n):
    lower = -1 * n
    upper = n
    # Sample ensures unique values
    return random.sample(range(lower, upper), n)

# Some helper code to write the results and easily display them later
def write_results_to_file(times_taken : dict, filename):
    with open(filename, 'w') as f:
        f.write("input,time\n")
        for key, value in times_taken.items():
            f.write(f'{key},{value}\n')

# Measures the time taken for a function to run and returns the average time taken
def measure_time(func, *args, repeats=5):
    total_time = 0
    # Benchmarks the function by running it multiple times on the same input size and averaging the time taken
    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / repeats

# Linear search which returns the index of the key if found, otherwise -1
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Benchmarks the best case scenario where the key is the first element
def benchmark_best_case(arr):
    linear_search(arr, arr[0]) # Make the first element the one we want

# Benchmarks the average case scenario where the key is a random element
def benchmark_average_case(arr, num_samples=10):
    random_keys = random.sample(arr, num_samples) # Randomly select 10 keys to search for
    total_time = 0
    for key in random_keys:
        total_time += measure_time(linear_search, arr, key)
    return total_time / num_samples

# Benchmarks the worst case scenario where the key is the last element
def benchmark_worst_case(arr):
    linear_search(arr, arr[-1]) # Make the last element the one we want

# Runs the benchmark for the best, average and worst case scenarios
def run_benchmark():
    time_taken_best = {}
    time_taken_average = {}
    time_taken_worst = {}
    for n in [100, 1000, 10000, 100000, 250000, 500000, 1000000]: # Indices I used last lab which worked well
        arr = random_distinct_integers(n)
        time_taken_best[n] = measure_time(benchmark_best_case, arr)
        time_taken_average[n] = benchmark_average_case(arr)
        time_taken_worst[n] = measure_time(benchmark_worst_case, arr)
    write_results_to_file(time_taken_best, 'best_case.csv')
    write_results_to_file(time_taken_average, 'average_case.csv')
    write_results_to_file(time_taken_worst, 'worst_case.csv')

if __name__ == '__main__':
    run_benchmark()