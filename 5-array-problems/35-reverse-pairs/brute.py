def reversePairs(arr:list[int]):
    n = len(arr)
    count = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] > 2*arr[j]:
                count += 1
    
    return count

print(reversePairs([1,3,2,3,1]))