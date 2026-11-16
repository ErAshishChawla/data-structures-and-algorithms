def searchMatrix(arr:list[list[int]], target:int) -> bool:
    rows = len(arr)

    if rows <= 0:
        return False

    cols = len(arr[0])

    possible_row_idx = -1
    low = 0
    high = rows - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid][0] <= target:
            possible_row_idx = mid
            low = mid + 1
        else:
            high = mid - 1

    if possible_row_idx == -1:
        return False

    low = 0
    high = cols - 1


    while low <= high:
        mid = (low + high) // 2

        if arr[possible_row_idx][mid] == target:
            return True
        elif arr[possible_row_idx][mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
