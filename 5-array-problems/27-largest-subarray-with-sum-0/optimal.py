def largestSubarrayWithSumZero(arr):
    n = len(arr)
    max_len = 0

    prefix_sum = dict()
    total = 0

    for i in range(0,n):
        total += arr[i]
        if total == 0:
            max_len = max(max_len, i+1)
        
        elif total in prefix_sum:
            total_idx = prefix_sum[total]
            max_len = max(max_len, i - total_idx)

        if total not in prefix_sum:
            prefix_sum[total] = i

    return max_len


arr1 = [15, -2, 2, -8, 1, 7, 10, 23]
arr2= [2, 10, 4]
arr3 = [1, 0, -4, 3, 1, 0]

print(largestSubarrayWithSumZero(arr1))
print(largestSubarrayWithSumZero(arr2))
print(largestSubarrayWithSumZero(arr3))