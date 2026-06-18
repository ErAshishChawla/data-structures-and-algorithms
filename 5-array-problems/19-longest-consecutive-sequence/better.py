def longestConsequtiveSequence(arr):
    sorted_arr = sorted(arr)

    n = len(arr)
    curr_len = 1
    max_len = 1

    for i in range(1, n):
        if sorted_arr[i-1] == sorted_arr[i]:
            continue

        if sorted_arr[i-1] + 1 == sorted_arr[i]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1

    return max_len


