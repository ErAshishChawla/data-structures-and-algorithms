def singleElement(arr: list[int]) -> int:
    n = len(arr)

    if n == 1:
        return arr[0]

    low = 0
    high = n - 1

    while low<=high:
        mid = (low + high) // 2

        if mid == 0 and arr[mid] != arr[mid + 1]:
            return arr[mid]
        elif mid == n-1 and arr[mid] != arr[mid - 1]:
            return arr[mid]
        elif arr[mid-1] != arr[mid] != arr[mid + 1]:
            return arr[mid]

        isEven = mid % 2 == 0

        if isEven:
            if arr[mid] == arr[mid + 1]:
                low = mid + 1
            else:
                high = mid-1
        else:
            if arr[mid] == arr[mid-1]:
                low = mid + 1
            else:
                high = mid - 1

print(singleElement([1,1,2,3,3,4,4,8,8]))
print(singleElement([1,1,2,2,3,3,4,4,8]))
print(singleElement([1,2,2,3,3,4,4,8,8]))
    







