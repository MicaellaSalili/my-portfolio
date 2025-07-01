import timeit

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def interpolation_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)