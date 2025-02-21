import timeit, scipy, numpy as np, matplotlib.pyplot as plt

def insertion_sort_trad(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1

def binary_search(array, elem, right):
    left = 0
    while left <= right:
        mid = int((left + right)/2)
        if array[mid] == elem:
            return mid
        elif array[mid] > elem:
            right = mid - 1
        else:
            left = mid + 1
    return left

def insertion_sort_bin(arr):
    for i in range(len(arr)):
        j = i - 1
        item = arr[i]
        loc = binary_search(arr, item, j)
        while j >= loc:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = item


def quad_func(x, a, b, c):
    return a * x ** 2 + b * x + c

def main():
    element_list = [3, 7, 13, 20, 40, 80]
    trad_time_list = []
    bin_time_list = []
    for num in element_list:
        print(f"Measuring performance of sort for {num} elements...")
        trad_time = 0
        bin_time = 0
        for i in range(10):
            rand_array = np.random.randint(0, 100, size = num)
            rand_array_2 = rand_array.copy()
            trad_time += timeit.timeit(stmt = "insertion_sort_trad(rand_array)", globals = {"insertion_sort_trad": insertion_sort_trad, "rand_array": rand_array}, number = 1)
            bin_time += timeit.timeit(stmt = "insertion_sort_bin(rand_array_2)", globals = {"insertion_sort_bin": insertion_sort_bin, "rand_array_2": rand_array_2}, number = 1)
        trad_time_list.append(trad_time/10)
        bin_time_list.append(bin_time/10)
    
    coeffs, covar = scipy.optimize.curve_fit(quad_func, element_list, trad_time_list)
    a_fit, b_fit, c_fit = coeffs
    x_fit = np.linspace(min(element_list), max(element_list))
    y_fit = quad_func(x_fit, a_fit, b_fit, c_fit)
    plt.plot(element_list, trad_time_list, label = 'Traditional', color = 'blue')
    plt.plot(x_fit, y_fit, label = 'Traditional Fit', color = 'green')
    coeffs, covar = scipy.optimize.curve_fit(quad_func, element_list, bin_time_list)
    a_fit, b_fit, c_fit = coeffs
    x_fit = np.linspace(min(element_list), max(element_list))
    y_fit = quad_func(x_fit, a_fit, b_fit, c_fit)
    plt.plot(element_list, bin_time_list, label = 'Binary', color = 'orange')
    plt.plot(x_fit, y_fit, label = 'Binary Fit', color = 'yellow')
    plt.legend()
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.title("Interpolation Sort")
    plt.show()

if __name__ == "__main__":
    main()

"""
4.  Both plots have a quadratic time complexity, but binary insertion sort is faster than traditional insertion sort. Binary insertion sort utilizes binary search instead of linear search to determine where each item should be inserted when sorting, which improves the time complexity of this step from O(n) to O(log n).
"""