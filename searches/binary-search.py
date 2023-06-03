import math

def binarySearch(haystack, needle):
    low = 0
    high = len(haystack)
    status = False

    while (low < high):
        mid = math.floor(low + (high - low) / 2)
        value = haystack[mid]

        if (needle == value):
            status = True
            break
        elif (needle < value):
            high = mid
        else:
            low = mid + 1

    return status