def countInversions(arr):
    n = len(arr)

    count = 0

    for i in range(0, n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                count += 1

    return count

arr1 = [2, 4, 1, 3, 5]
arr2 = [2, 3, 4, 5, 6]
arr3 = [10, 10, 10]

print(countInversions(arr1))
print(countInversions(arr2))
print(countInversions(arr3))