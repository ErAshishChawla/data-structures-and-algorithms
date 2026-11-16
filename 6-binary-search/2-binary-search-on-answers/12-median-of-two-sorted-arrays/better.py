def median(arr1:list[int], arr2:list[int]) -> float:
    m = len(arr1)
    n = len(arr2)
    total_len = m + n

    idx = 0
    i = 0
    j = 0

    isEven = total_len % 2 == 0
    prev_val = - 1
    median_idx = total_len // 2

    while i < m and j < n:
        val = -1
        if arr1[i] <= arr2[j]:
            val = arr1[i]
            i+=1
        else:
            val = arr2[j]
            j+=1
        
        if isEven and idx == median_idx - 1:
            prev_val = val
        elif isEven and idx == median_idx:
            return (prev_val + val) / 2
        elif not isEven and idx == median_idx:
            return val
        
        idx += 1

    while i < m:
        val = arr1[i]
        i += 1

        if isEven and idx == median_idx - 1:
            prev_val = val
        elif isEven and idx == median_idx:
            return (prev_val + val) / 2
        elif not isEven and idx == median_idx:
            return val
        
        idx += 1
    
    while j < n:
        val = arr2[j]
        j += 1

        if isEven and idx == median_idx - 1:
            prev_val = val
        elif isEven and idx == median_idx:
            return (prev_val + val) / 2
        elif not isEven and idx == median_idx:
            return val
        
        idx += 1

    return -1




print(median([1,3], [2]))
print(median([1,2], [3,4]))