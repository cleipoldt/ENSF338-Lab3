import timeit, scipy, numpy as np, matplotlib.pyplot as plt

def insertion_sort_trad(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
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

def main():
    element_list = [5, 10, 30, 80]
    trad_time_list = []
    bin_time_list = []
    for num in element_list:
        print(f"Measuring performance of sort for {num} elements...")
        trad_time = 0
        bin_time = 0
        for i in range(2):
            rand_array = np.random.randint(num, size = num)
            rand_array_2 = rand_array
            trad_time += timeit.timeit(stmt = "insertion_sort_trad(rand_array)", globals = {"insertion_sort_trad": insertion_sort_trad, "rand_array": rand_array})
            bin_time += timeit.timeit(stmt = "insertion_sort_bin(rand_array)", globals = {"insertion_sort_bin": insertion_sort_bin, "rand_array": rand_array_2})
        trad_time_list.append(trad_time/2)
        bin_time_list.append(bin_time/2)
    
    plt.plot(element_list, trad_time_list, label = 'Traditional')
    plt.plot(element_list, bin_time_list, label = 'Binary', color = 'orange')
    plt.xlabel("Number of elements")
    plt.ylabel("Time")
    plt.title("Interpolation Search")
    plt.show()

if __name__ == "__main__":
    main()

"""
4.  
"""