def rotationCount(arr:list[int]) -> int:
    n = len(arr)

    low = 0
    high = n - 1

    mini = float("Inf")
    mini_idx = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < mini:
            mini = arr[mid]
            mini_idx = mid

        if arr[low] <= arr[mid]:
            if arr[mid] <= arr[high]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            high = mid - 1

    return mini_idx
