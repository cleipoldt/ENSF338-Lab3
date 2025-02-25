import random
import matplotlib.pyplot as plt
import numpy as np


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0  
    swaps = 0       

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1 
            if arr[j] > arr[j + 1]:
        
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swaps += 1  

    return comparisons, swaps

sizes = [10, 20, 35, 55, 80] 
comparison_counts = []
swap_counts = []

for size in sizes:
    arr = [random.randint(1, 100) for _ in range(size)]  
    comparisons, swaps = bubble_sort(arr.copy())
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)
    
print(comparison_counts)
print(swap_counts)

comp_fit = np.polyfit(sizes, comparison_counts, 2)
swap_fit = np.polyfit(sizes, swap_counts, 2)

comp_poly = np.poly1d(comp_fit)
swap_poly = np.poly1d(swap_fit)

sizes_smooth = np.linspace(min(sizes), max(sizes), 100)  
comp_smooth = comp_poly(sizes_smooth)
swap_smooth = swap_poly(sizes_smooth)

plt.figure(figsize=(10, 5))

plt.plot(sizes, comparison_counts, 'bo', label="Actual Comparisons")
plt.plot(sizes_smooth, comp_smooth, 'b--', label="Interpolated Comparisons")

plt.plot(sizes, swap_counts, 'ro', label="Actual Swaps")
plt.plot(sizes_smooth, swap_smooth, 'r--', label="Interpolated Swaps")

plt.xlabel("Input Size (n)")
plt.ylabel("Operations Count")
plt.title("Bubble Sort Complexity Analysis with Interpolation")
plt.legend()
plt.grid()
plt.show()