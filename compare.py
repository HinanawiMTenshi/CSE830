import time
import random
import matplotlib.pyplot as plt

   
def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# Function to generate random arrays
def generate_random_array(n):
    return [random.randint(0, 10000) for _ in range(n)]

# Function to measure execution time
def measure_time(sort_function, arr, iterations=1, **kwargs):
    start_time = time.time()
    for _ in range(iterations):
        arr_copy = arr.copy()
        sort_function(arr_copy, **kwargs)
    end_time = time.time()
    return (end_time - start_time) / iterations

# Main function to compare sort algorithms
def compare_sorts(ranges, iterations=1):
    merge_times = []
    insertion_times = []

    for n in ranges:
        arr = generate_random_array(n)

        merge_time = measure_time(mergeSort, arr, iterations, l=0, r=n-1)
        insertion_time = measure_time(insertionSort, arr, iterations)

        merge_times.append(merge_time)
        insertion_times.append(insertion_time)

    plt.plot(ranges, merge_times, label='Merge Sort', marker='o')
    plt.plot(ranges, insertion_times, label='Insertion Sort', marker='x')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Merge Sort vs Insertion Sort Runtime Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


input_sizes = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]

compare_sorts(input_sizes,1000)
