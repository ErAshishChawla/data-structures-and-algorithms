def peakElement(arr:list[int]) -> int:
    n = len(arr)

    if n == 1:
        return 0

    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        if mid == 0 and arr[mid] > arr[mid + 1]:
            return mid
        elif mid == n-1 and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid


        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    return

print(peakElement([1,2,3,1]))
print(peakElement([1,2,1,3,5,6,4]))
print(peakElement([10, 8, 6, 4, 2, 3, 5, 7, 9]))