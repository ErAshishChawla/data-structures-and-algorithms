def sweep(arr, start, end, step):
    curr = 1
    maxi = float("-Inf")

    for i in range(start, end, step):
        if arr[i] == 0:
            curr = 1
            maxi = max(maxi, 0)

        else:
            curr = curr * arr[i]
            maxi = max(maxi, curr)

    return maxi

def maxProductSubarray(arr:list[int]) -> int:
    n = len(arr)
    
    if n <= 0:
        return 0

    if n == 1:
        return arr[0]

    max1 = sweep(arr, 0, n, 1)
    max2 = sweep(arr, n-1, -1, -1)

    return max(max1, max2)
