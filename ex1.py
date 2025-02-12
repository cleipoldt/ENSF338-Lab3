import sys
sys.setrecursionlimit(20000)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)/2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return 

'''
merge() not correct, will still have to edit later. I'm not seeing the "merge" part in either function I thought the 
merge sort would be in the merge_sort function but apparently it's in neither so I will need to figure that out
'''

def merge(arr, low, mid, high):
    #for case when array only has 2 elements
    if len(arr) == 2:
        if (arr[low] < arr[high]):
            return
        else:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp

    '''
    if array has 3 or more elements (therefore at least one subarray will have 2 or more elements by pigeonhole)
    so in this case we just look at the first element of the subarrays because they should already be sorted in the 
    if case above (if len(arr) == 2)?
    '''

    return 

def main():
    return 0

if __name__ == "__main__":
    main()