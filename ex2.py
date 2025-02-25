import sys
import random
import matplotlib.pyplot as plt
import timeit

sys.setrecursionlimit(5000)

# bubble sort 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# quick sort

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    
    mid = (low + high) // 2
    arr[low], arr[mid] = arr[mid], arr[low]
    
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while right >= left and arr[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


# Function that generates test cases with a default value of average
def generate_test_case(size, case_type="average", algorithm="bubble"):
    arr = list(range(size))
    
    if algorithm == "bubble":
        if case_type == "best":
            return arr
        elif case_type == "worst":
            return arr[::-1]
        else:
            random.shuffle(arr)
            return arr
        
    elif algorithm == "quick":
        if case_type == "best":
            return arr
        elif case_type == "worst":
            return arr[::-1]
        else:
            random.shuffle(arr)
            return arr

    random.shuffle(arr)
    return arr

# function that measures the time it takes to sort different sizes of arrays using different algorithms and different case_types

def measure_time(sort_function, arr):
    return timeit.timeit(lambda: sort_function(arr.copy()), number = 1)

sizes = list(range(5, 30, 5)) + list(range(30, 180, 10))

results = {
    "bubble": {"best": [], "worst": [], "average": []},
    "quick": {"best": [], "worst": [], "average": []}
}

# For each case type, 20 different sizes get executed

for case_type in ["best", "worst", "average"]:
    for size in sizes:
        test_case_bubble = generate_test_case(size, case_type, algorithm="bubble")
        test_case_quick = generate_test_case(size, case_type, algorithm="quick")

        bubble_time = measure_time(bubble_sort, test_case_bubble)

        quick_time = measure_time(lambda arr: quicksort(arr, 0, len(arr) - 1), test_case_quick)

        results["bubble"][case_type].append(bubble_time)
        results["quick"][case_type].append(quick_time)

print("completed all cases")

# create plots

for case_type in ["best", "worst", "average"]:
    plt.figure()
    plt.plot(sizes, results["bubble"][case_type], label="Bubble Sort", marker='o', color='blue')
    plt.plot(sizes, results["quick"][case_type], label="Quick Sort", marker='s', color='red')
    
    for i, size in enumerate(sizes):
        if results["bubble"][case_type][i] < results["quick"][case_type][i]:
            plt.scatter(size, results["bubble"][case_type][i], color='blue', edgecolors='black', zorder=3)
        else:
            plt.scatter(size, results["quick"][case_type][i], color='red', edgecolors='black', zorder=3)

    plt.axvline(x=30, color='green', linestyle='dashed', label='Threshold = 30')
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Bubble Sort vs Quick Sort ({case_type} Case)")
    plt.legend()
    plt.show()


""" Based on the time plots, we chose a threshold of 30 elements to determing whether or not
the input is small. From the course notes we know that bubble sort has a O(n^2) time complexity
which would make it efficient for smaller input sizes

Quick sort has a best case, as well as average case time complexity of O(nlog n) making it efficient
for larger inputs.

The plot indicates that for sizes below 30, Bubble sort and Quick sort perform very similarly.
For some cases, Bubble sort even outperforms Quick sort. However, for any input larger than 30, Quick sort
performs much better than bubble sort.
"""





