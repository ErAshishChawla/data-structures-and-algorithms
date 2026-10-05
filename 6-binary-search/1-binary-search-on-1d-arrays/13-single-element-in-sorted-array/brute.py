def singleElement(arr:list[int]) -> int:
    n = len(arr)

    single = arr[n-1]

    for i in range(1, n, 2):
        if arr[i-1] != arr[i]:
            single = arr[i-1]
            break

    return single

print(singleElement([1,1,2,3,3,4,4,8,8]))
print(singleElement([1,1,2,2,3,3,4,4,8]))