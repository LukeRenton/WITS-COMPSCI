import random
import time

def random_distinct_integers(n):
    lower = -1 * n
    upper = n
    # Sample ensures unique values
    return random.sample(range(lower, upper), n)

def best_case_array(n):
    return list(range(n))
    
def bubble_sort_no_escape_clause(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

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

def measure_time(func, *args, best_case, repeats=3):
    total_time = 0
    # Benchmarks the function by running it multiple times on the same input size and averaging the time taken
    for _ in range(repeats):
        arr = random_distinct_integers(args[0]) if not best_case else best_case_array(args[0])
        start = time.perf_counter()
        func(arr)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / repeats

def write_results_to_file(times_taken : dict, filename):
    with open(filename, 'w') as f:
        f.write("input,time\n")
        for key, value in times_taken.items():
            f.write(f'{key},{value}\n')
            
def run_benchmark():
    time_taken_bubble_sort_no_escape_clause = {}
    time_taken_bubble_sort_with_escape_clause_best_case = {}
    time_taken_bubble_sort_with_escape_clause = {}
    # These seemed to be the most significant samples to test
    for n in [100, 500, 1000, 1500, 3000, 5000]:
        time_taken_bubble_sort_no_escape_clause[n] = measure_time(bubble_sort_no_escape_clause, n, best_case=False) 
        time_taken_bubble_sort_with_escape_clause_best_case[n] = measure_time(bubble_sort_with_escape_clause, n, best_case=True)
        time_taken_bubble_sort_with_escape_clause[n] = measure_time(bubble_sort_with_escape_clause, n, best_case=False)
        print(f'Finished benchmarking for n={n}, bubble_sort_no_escape_clause={time_taken_bubble_sort_no_escape_clause[n]}, bubble_sort_with_escape_clause_best_case={time_taken_bubble_sort_with_escape_clause_best_case[n]}, bubble_sort_with_escape_clause={time_taken_bubble_sort_with_escape_clause[n]}')
    write_results_to_file(time_taken_bubble_sort_no_escape_clause, 'bubble_sort_no_clause.csv')
    write_results_to_file(time_taken_bubble_sort_with_escape_clause_best_case, 'bubble_sort_best_case.csv')
    write_results_to_file(time_taken_bubble_sort_with_escape_clause, 'bubble_sort.csv')

if __name__ == '__main__':
    run_benchmark()
