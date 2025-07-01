import random
import time

# Bubble sort with no escape clause algorithm
def bubble_sort_no_escape_clause(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# returns a list of n distinct integers in a random order
def random_distinct_integers(n):
    lower = -1 * n
    upper = n
    return random.sample(range(lower, upper), n)

# helper function to measure the time taken for a function to run (in our case the buble sort), averaged over 'repeats' number of runs
def measure_time(func, n, repeats=3):
    total_time = 0
    for _ in range(repeats):
        arr = random_distinct_integers(n)
        start = time.perf_counter()
        func(arr)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / repeats

# just writes results into a file
def write_results_to_file(times_taken : dict, filename):
    with open(filename, 'w') as f:
        f.write("input,time\n")
        for key, value in times_taken.items():
            f.write(f'{key},{value}\n')

if __name__ == '__main__':
    time_taken_bubble_sort_no_escape_clause = {}
    for n in [100, 500, 1000, 1500, 3000, 5000, 8000, 10000]:
        time_taken_bubble_sort_no_escape_clause[n] = measure_time(bubble_sort_no_escape_clause, n) 
    write_results_to_file(time_taken_bubble_sort_no_escape_clause, 'bubble_sort_no_escape_clause.csv')