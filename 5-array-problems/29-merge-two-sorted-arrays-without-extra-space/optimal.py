def merge(arr1:list[int], arr2:list[int]) -> None:
    n = len(arr1)
    m = len(arr2)

    for i in range(0, min(n,m)):
        one_idx = n - i -1
        two_idx = i

        if arr1[one_idx] > arr2[two_idx]:
            arr1[one_idx], arr2[two_idx] = arr2[two_idx], arr1[one_idx]
        else:
            break

    arr1.sort()
    arr2.sort()

    return

arr1 = [10]
arr2 = [1,2,3]

merge(arr1, arr2)

print(arr1)
print(arr2)