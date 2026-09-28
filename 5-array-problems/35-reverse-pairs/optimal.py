def mergeAndCount(left:list[int], right:list[int]):
    n = len(left)
    m = len(right)

    count = 0
    x = 0
    for y in range(0, m):
        while x < n and left[x] <= 2 * right[y]:
            x += 1
        count += n - x

    merged = []

    i = 0
    j = 0
    while i < n and j < m:
        if left[i] <= right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    for x in range(i, n):
        merged.append(left[x])
    
    for y in range(j, m):
        merged.append(right[y])

    return merged, count

def mergeSort(arr:list[int]):
    n = len(arr)

    if n <=1:
        return arr, 0

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    sorted_left, left_count = mergeSort(left)
    sorted_right, right_count = mergeSort(right)

    merged, count = mergeAndCount(sorted_left, sorted_right)

    return merged, left_count + right_count + count

def reversePairs(arr:list[int]):
    m, c = mergeSort(arr)
    return c

print(reversePairs([1,3,2,3,1]))
print(reversePairs([2,4,3,5,1]))