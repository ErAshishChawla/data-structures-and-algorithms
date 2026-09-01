def majorityElement(arr):
    n = len(arr)

    result = [] # max 2 elements will be stored here
    freq_map = dict()

    limit = n // 3

    for val in arr:
        freq_map[val] = freq_map.get(val, 0) + 1
        if freq_map[val] > limit and val not in result:
            result.append(val)

    return result

arr = [1,2,3,1,1,2,2,2,1]
print(majorityElement(arr))