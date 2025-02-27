import json, timeit, matplotlib.pyplot as plt

def binary_search(arr, elem, first_mid):
    low = 0
    high = len(arr) - 1
    mid = first_mid
    while low <= high:
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1
        mid = int((low + high)/2)
    return -1

def main():
    file_data = open('ex7data.json')
    file_tasks = open('ex7tasks.json')
    data = json.load(file_data)
    tasks = json.load(file_tasks)
    file_data.close()
    file_tasks.close()

    time_list_1, time_list_2, time_list_3 = [], [], []
    mid_list = [int((len(data) - 1)/4), int((len(data) - 1) * 3 / 4), int((len(data) - 1)/2)]
    
    for task in tasks:
        print(f"Searching for {task} in data...")
        time_list_1.append(timeit.timeit(stmt = 'binary_search(data, task, mid_list[0])', number = 1, globals = {'data': data, 'task': task, 'mid_list': mid_list, 'binary_search': binary_search}))
        time_list_2.append(timeit.timeit(stmt = 'binary_search(data, task, mid_list[1])', number = 1, globals = {'data': data, 'task': task, 'mid_list': mid_list, 'binary_search': binary_search}))
        time_list_3.append(timeit.timeit(stmt = 'binary_search(data, task, mid_list[2])', number = 1, globals = {'data': data, 'task': task, 'mid_list': mid_list, 'binary_search': binary_search}))
    for i in range(len(tasks)):
        min_time = min([time_list_1[i], time_list_2[i], time_list_3[i]])
        print(f"The best midpoint for finding {tasks[i]} is ", end = "")
        if min_time == time_list_1[i]:
            print("the element at 1/4 of the array.")
        elif min_time == time_list_2[i]:
            print("the element at 3/4 of the array.")
        else:
            print("the middle element.")
        

    plt.xlabel("Task Value")
    plt.ylabel("Time")
    plt.title("Binary Search with Different Midpoints")
    plt.scatter(tasks, time_list_1, label = 'Element at 1/4', s = 5, color = 'purple')
    plt.scatter(tasks, time_list_2, label = 'Element at 3/4', s = 5, color = 'green')
    plt.scatter(tasks, time_list_3, label = 'Middle Element', s = 5, color = 'orange')
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()

"""
4.  Having the middle element to be the initial midpoint delivers the best performance for the most part, as it narrows the possible range the most in the first iteration compared to the other midpoints. The other midpoints cause more outlying points on the plot, that show the search taking more time due to the selection of the midpoint the first iteration. The data size of the provided json file is very large, so the initial midpoint does not make a huge difference in performance, but the middle element still shows to be the most consistent performer.
"""
