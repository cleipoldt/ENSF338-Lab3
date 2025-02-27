import sys
sys.setrecursionlimit(20000)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)/2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return 


def merge(arr, low, mid, high):
    leftArr = []
    rightArr = []

    for i in range(low, mid-low+1):
        leftArr[i] = arr[low + i]

    for j in range(mid+1, high+1):
        rightArr[j] = arr[mid+1+j]
    
    i = 0     
    j = 0     
    k = low    

    while i < (mid-low+1) and j < (mid+1+j):
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    while i < (mid-low+1):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < (mid+1+j):
        arr[k] = rightArr[j]
        j += 1
        k += 1

    return 

def main():
    return 0

if __name__ == "__main__":
    main()