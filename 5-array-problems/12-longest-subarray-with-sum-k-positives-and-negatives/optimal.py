def longestSubarray(arr, k):
    n = len(arr)
    max_len = 0

    sum = 0
    prefix_sums = dict()

    for i in range(n):
        sum += arr[i]

        if sum == k:
            max_len = max(max_len, i+1)
        else:
            prefix_sum = sum - k
            if prefix_sum in prefix_sums:
                max_len = max(max_len, i - prefix_sums[prefix_sum])

        if sum not in prefix_sums:
            prefix_sums[sum] = i

    return max_len

arr= [10, 5, 2, 7, 1, -10]
print(longestSubarray(arr, 15))