def maxConsecutiveOnes(arr):
    max_count = float("-Inf")
    count = 0

    for val in arr:
        if val == 0:
            count = 0
        else:
            count += 1
        max_count = max(max_count, count)

    return max_count