def longestSubarray(arr, k):
    n = len(arr)

    left = 0
    curr_sum = 0
    max_len = 0

    for right in range(n):
        curr_sum += arr[right]

        while curr_sum > k and left <= right:
            curr_sum -= arr[left]
            left += 1

        if curr_sum == k:
            max_len = max(max_len, right-left + 1)

    return max_len

arr = [1, 0, 2, 0, 0, 3, 1]
k = 3

print(longestSubarray(arr, k))
