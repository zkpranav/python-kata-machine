def quickSort(arr):
    if (len(arr) < 2):
        return

    _sort(arr, 0, len(arr) - 1)

def _sort(arr, low, high):
    if (low >= high):
        return
    
    pivotIdx = _partition(arr, low, high)
    _sort(arr, low, pivotIdx - 1)
    _sort(arr, pivotIdx + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]
    idx = low - 1

    for i in range(low, high):
        if (arr[i] <= pivot):
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
    
    idx += 1
    arr[high] = arr[idx]
    arr[idx] = pivot

    return idx