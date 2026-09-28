def largestSubarrayWithSumZero(arr):
    n = len(arr)
    max_len = 0

    for i in range(0, n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total == 0:
                max_len = max(max_len, j - i + 1)
    return max_len


arr1 = [15, -2, 2, -8, 1, 7, 10, 23]
arr2= [2, 10, 4]
arr3 = [1, 0, -4, 3, 1, 0]

print(largestSubarrayWithSumZero(arr1))
print(largestSubarrayWithSumZero(arr2))
print(largestSubarrayWithSumZero(arr3))