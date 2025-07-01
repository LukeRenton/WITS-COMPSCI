import random
import time

# Merge function
def merge(arr, left, mid, right):
    # Create a temporary array to store the merged array
    temp = [0] * (right - left + 1)
    
    # Copy left half into temp array
    for i in range(mid - left + 1):
        temp[i] = arr[left + i]
    
    # Copy right half into temp array in reverse order
    for j in range(right - mid):
        temp[(right - left) - j] = arr[mid + 1 + j]
    
    i = 0
    j = right - left
    
    # Merge back to arr
    for k in range(left, right + 1):
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j -= 1

# Merge sort algorithm
def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        
        # Recursively sort the first and second halves
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        
        # Merge the sorted halves
        merge(arr, left, mid, right)

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
        func(arr, 0, len(arr) - 1)
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
    time_taken_merge_sort = {}
    
    # Test for different input sizes
    for n in [100, 1000, 10000, 100000, 250000, 500000, 1000000]:
        time_taken_merge_sort[n] = measure_time(mergeSort, n)
    
    # Write the results to a CSV file
    write_results_to_file(time_taken_merge_sort, 'merge_sort.csv')