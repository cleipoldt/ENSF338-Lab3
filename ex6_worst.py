import sys, timeit, numpy as np, matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

def linear_search(arr, elem):
    index = 0
    for num in arr:
        if num == elem:
            return index
        index += 1
    return -1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def binary_search(arr, elem):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high)/2)
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    input_list = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    linear_list = []
    binary_list = []
    for num in input_list:
        print(f"Measuring performance of search in {num} elements...")
        linear_time = 0
        binary_time = 0
        element_list = [x for x in range(num)]
        for i in range(100):
            item = np.random.choice(element_list)
            linear_time += timeit.timeit(stmt = 'linear_search(element_list, item)', number = 1, globals = {'item': item, 'linear_search': linear_search, 'element_list': element_list})
            binary_time += timeit.timeit(stmt = 'quick_sort(element_list, 0, len(element_list)-1);binary_search(element_list, item)', number = 1, globals = {'item': item, 'quick_sort': quick_sort, "binary_search": binary_search, "element_list": element_list})
        linear_list.append(linear_time)
        binary_list.append(binary_time)

    
    plt.plot(input_list, linear_list, label = 'Linear Search', color = 'red')
    plt.plot(input_list, binary_list, label = 'Quick Sort + Binary Search', color = 'blue')
    plt.legend()
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.title('Sorting + Searching')
    plt.show()

if __name__ == "__main__":
    main()

"""
5.  The quick sort algorithm implemented in this exercise chooses the last element of the array or subarray as the pivot. The input that causes quick sort to be in its worst case is when the pivot partitions the array into subarrays of size n-1 and 0. Thus, an array sorted from least to greatest as input causes the quicksort with the pivot at the last element to incur its worst case performance. Even in the average case, the linear search was faster than the quick sort + binary search, but in the worst case of the quick sort, its time complexity goes to O(n^2), further highlighting linear search as the better choice.
"""
