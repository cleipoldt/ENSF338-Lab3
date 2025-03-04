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
        item = np.random.choice(element_list)
        for i in range(100):
            np.random.shuffle(element_list)
            linear_time += timeit.timeit(stmt = 'linear_search(element_list, item)', number = 1, globals = {'item': item, 'linear_search': linear_search, 'element_list': element_list})
            np.random.shuffle(element_list)
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
4.  The exercise involved shuffling the array every time, so for the quick sort + binary search, the time complexities for both the sort and the search was accounted for, making the quick sort + binary search less effective than the linear search. If the exercise was modified so the array was only shuffled when the input size changed, the quick sort + binary search would have been much faster than the linear search. In the average case, the time complexities of quick sort, binary search, and linear search are O(n * log n), O(log n), and O(n).
"""
