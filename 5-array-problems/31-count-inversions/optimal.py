def mergeAndCount(left:list[int], right:list[int], cnt: int):
    n = len(left)
    m = len(right)

    count = cnt
    
    i = 0
    j = 0

    merged = []

    while i < n and j < m:
        if left[i] <= right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            count += n - i
            j+=1

    for x in range(i,n):
        merged.append(left[x])

    for y in range(j,m):
        merged.append(right[y])

    return [merged, count]

def mergeSort(arr:list[int], count:int):
    n = len(arr)

    if n <= 1:
        return [arr, 0]

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    [sorted_left, left_count] = mergeSort(left, count)
    [sorted_right, right_count] = mergeSort(right, count)

    return mergeAndCount(sorted_left, sorted_right, left_count + right_count)


def countInversions(arr:list[int]) -> int:
    [merged, count] = mergeSort(arr, 0)
    return count

arr1 = [2, 4, 1, 3, 5]
arr2 = [2, 3, 4, 5, 6]
arr3 = [10, 10, 10]

print(countInversions(arr1))
print(countInversions(arr2))
print(countInversions(arr3))