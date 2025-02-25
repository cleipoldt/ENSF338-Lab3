import random
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0  # Counter for comparisons
    swaps = 0        # Counter for swaps

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1 
            if arr[j] > arr[j + 1]:
                # Swap elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swaps += 1  

    return comparisons, swaps  # Return sorted array along with counts

# Test bubble sort on various input sizes
sizes = [10, 20, 35, 55, 80]  # Input sizes
comparison_counts = []
swap_counts = []

for size in sizes:
    arr = [random.randint(1, 100) for _ in range(size)]  # Generate random array
    comparisons, swaps = bubble_sort(arr.copy())  # Run bubble sort
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)
    
print(comparison_counts)
print(swap_counts)

plt.figure(figsize=(10, 5))
plt.plot(sizes, comparison_counts, marker='o', label="Comparisons")
plt.plot(sizes, swap_counts, marker='s', label="Swaps")

plt.xlabel("Input Size (n)")
plt.ylabel("Operations Count")
plt.title("Bubble Sort Complexity Analysis")
plt.legend()
plt.grid()
plt.show()