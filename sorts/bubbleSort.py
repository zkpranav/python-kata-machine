def bubbleSort(arr):
    if (len(arr) < 2):
        return
    
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if (arr[j] > arr[j + 1]):
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
