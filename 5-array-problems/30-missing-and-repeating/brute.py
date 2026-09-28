def missingAndRepeating(arr):
    n = len(arr)

    curr_sum = 0
    exp_sum = (n * (n+1))//2

    freq_map = dict()
    dup_val = 0

    for val in arr:
        if val not in freq_map:
            freq_map[val] = 1
        else:
            freq_map[val] = freq_map[val] + 1
            dup_val = val
        
        curr_sum += val

    missing_val = exp_sum - curr_sum + dup_val

    return [dup_val, missing_val]

arr = [4, 3, 6, 2, 1, 1]
print(missingAndRepeating(arr))
