def missingAndRepeating(arr):
    n = len(arr)

    curr_sum = 0
    curr_sq_sum = 0

    exp_sum = (n * (n+1)) // 2
    exp_sq_sum = (n * (n+1) * (2*n + 1)) // 6

    for val in arr:
        curr_sum += val
        curr_sq_sum += val ** 2

    diff_of_sq = exp_sq_sum - curr_sq_sum
    diff = exp_sum - curr_sum

    factor_of_diff = (exp_sq_sum - curr_sq_sum) // (exp_sum - curr_sum)
    repeating = (factor_of_diff - (diff)) // 2
    missing = diff + repeating

    return [repeating, missing]

arr = [4, 3, 6, 2, 1, 1]
print(missingAndRepeating(arr))
