import random
import math
import time

# Helper function to generate random points in 2D plane
def generate_random_points(n):
    return [(random.randint(-n, n), random.randint(-n, n)) for _ in range(n)]

# Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Brute Force Closest Pair Algorithm
def brute_force_closest_pair(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    
    # Return the closest pair and the distance between them 
    return pair, min_dist

# Final Closest Pair Algorithm (Divide and Conquer)
def closest_pair(points : list):
    points.sort(key=lambda x: x[0]) # Sort points by x-coordinate
    return closest_pair_recursive(points)

# Recursive function to find closest pair of points
def closest_pair_recursive(points):
    if len(points) <= 3:
        return brute_force_closest_pair(points)
    
    # Divide the points into two halves
    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]
    
    # Recursively find closest pair in left and right halves
    (p1_left, d1) = closest_pair_recursive(left_points)
    (p2_right, d2) = closest_pair_recursive(right_points)
    
    # Find minimum distance between left and right closest pairs
    min_dist = min(d1, d2)
    pair = p1_left if d1 < d2 else p2_right
    
    # Check the strip region across the midpoint
    mid_x = points[mid][0]
    strip_points = [point for point in points if abs(point[0] - mid_x) < min_dist]
    strip_points.sort(key=lambda x: x[1]) # Sort by y-coordinate
    
    # Find the closest pair in the strip region
    for i in range(len(strip_points)):
        for j in range(i + 1, min(i + 7, len(strip_points))):
            dist = euclidean_distance(strip_points[i], strip_points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (strip_points[i], strip_points[j])
    
    # Return the closest pair and the distance between them 
    return pair, min_dist

# helper function to measure the time taken for a function to run (in our case the buble sort), averaged over 'repeats' number of runs
def measure_time(func, points, repeats=3):
    total_time = 0
    for _ in range(repeats):
        start = time.perf_counter()
        func(points)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / repeats

# Function to write results to file
def write_results_to_file(times_taken, filename):
    with open(filename, 'w') as f:
        f.write("input,time\n")
        for key, value in times_taken.items():
            f.write(f'{key},{value}\n')

# Testing and recording the time for different n values
if __name__ == '__main__':
    time_taken_brute_force = {}
    time_taken_divide_conquer = {}

    for p in range(2, 13):  
        n = 2 ** p 
        points = generate_random_points(n)        
        time_taken_brute_force[n] = measure_time(brute_force_closest_pair, points)
        time_taken_divide_conquer[n] = measure_time(closest_pair, points)
    
    # Write results to files
    write_results_to_file(time_taken_brute_force, 'brute_force_closest_pair.csv')
    write_results_to_file(time_taken_divide_conquer, 'divide_conquer_closest_pair.csv')
