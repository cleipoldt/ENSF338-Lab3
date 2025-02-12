

def insertion_sort_trad(arr):
    i = 1
    while i < len(arr):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
        i += 1
    return arr

def binary_search()

def insertion_sort_bin(arr):
    i = 1
    while i < len(arr):
        key = arr[i]

    return arr

def main():
    test = [4, 6, 2, 4, 10, 34, 1]
    print(insertion_sort_trad(test))

if __name__ == "__main__":
    main()