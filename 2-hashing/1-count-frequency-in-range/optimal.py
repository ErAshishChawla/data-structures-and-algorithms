def frequencyCount(arr:list[int]):
    n = len(arr) # 1-based indexing
    freq = [0] * n

    for num in arr:
        freq[num - 1] += 1

    return freq

print(frequencyCount([2, 3, 2, 3, 5]))

