def median(arr1:list[int], arr2:list[int]) -> int:
    m = len(arr1)
    n = len(arr2)

    merged = []

    i = 0
    j = 0

    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1

    for x in range(i, m):
        merged.append(arr1[x])
    
    for y in range(j, n):
        merged.append(arr2[y])


    k = len(merged)
    middle = k // 2

    if k % 2 == 0:
        return (merged[middle] + merged[middle - 1]) / 2
    else:
        return merged[middle]

print(median([1,3], [2]))
print(median([1,2], [3,4]))