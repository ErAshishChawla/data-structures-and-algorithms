def peakElement(arr:list[int]) -> int:
    n = len(arr)

    if n == 1:
        return 0

    for i in range(0, n):
        if i == 0 and arr[i] > arr[i+1]:
            return i
        
        elif i == n-1 and arr[i] > arr[i-1]:
            return i

        else:
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i

print(peakElement([1,2,3,1]))
print(peakElement([1,2,1,3,5,6,4]))
