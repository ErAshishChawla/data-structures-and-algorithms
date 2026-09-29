def floorCeil(arr:list[int], target:int):
    n = len(arr)

    low = 0
    high = n-1

    floor=-1
    ceil=-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            floor = arr[mid]
            ceil = arr[mid]
            break
        elif arr[mid] < target:
            floor = arr[mid]
            low = mid+1
        else:
            ceil = arr[mid]
            high = mid - 1

    return floor, ceil
