def longestConsequtiveSequence(arr):
    unique = set(arr)
    max_len = 1

    for val in unique:
        is_starting = False if val - 1 in unique else True

        if is_starting:
            curr_len = 1
            next_val = val + 1

            while next_val in unique:
                curr_len += 1
                next_val += 1
            
            max_len = max(max_len, curr_len)

    return max_len