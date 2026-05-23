def maximumSubarraySum(arr):
    curr_sum = 0
    max_sum = float("-Inf")

    for val in arr:
        if curr_sum < 0:
            curr_sum = 0

        curr_sum += val
        max_sum = max(curr_sum, max_sum)

    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarraySum(arr))