def maximumSubarraySum(arr):
    n = len(arr)
    max_sum = float("-Inf")

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            max_sum = max(curr_sum, max_sum)

    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarraySum(arr))