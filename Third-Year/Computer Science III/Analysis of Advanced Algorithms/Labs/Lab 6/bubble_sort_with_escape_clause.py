import random
import time

# bubble sort with escape clause algorithm
def bubble_sort_with_escape_clause(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# returns a list of n distinct integers in a random order
def random_distinct_integers(n):
    lower = -1 * n
    upper = n
    return random.sample(range(lower, upper), n)

# returns a list of n integers in ascending order (best case for bubble sort)
def best_case_array(n):
    return list(range(n))

# helper function to measure the time taken for a function to run (in our case the buble sort), averaged over 'repeats' number of runs
def measure_time(func, arr, repeats=3):
    total_time = 0
    for _ in range(repeats):
        start = time.perf_counter()
        func(arr)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / repeats

# just writes results into a file
def write_results_to_file(times_taken: dict, filename):
    with open(filename, 'w') as f:
        f.write("input,time\n")
        for key, value in times_taken.items():
            f.write(f'{key},{value}\n')

if __name__ == '__main__':
    time_taken_bubble_sort = {}
    time_taken_bubble_sort_best_case = {}
    for n in [100, 500, 1000, 1500, 3000, 5000, 8000, 10000, 20000, 30000]:
        arr = random_distinct_integers(n)
        time_taken_bubble_sort[n] = measure_time(bubble_sort_with_escape_clause, arr)
        
        arr = best_case_array(n)
        time_taken_bubble_sort_best_case[n] = measure_time(bubble_sort_with_escape_clause, arr)

    write_results_to_file(time_taken_bubble_sort, 'bubble_sort_with_escape_clause.csv')
    write_results_to_file(time_taken_bubble_sort_best_case, 'bubble_sort_with_escape_clause_best_case.csv')
