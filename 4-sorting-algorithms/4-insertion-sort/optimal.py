def insertionSort(arr:list[int]) -> None:
    n = len(arr)

    for i in range(1, n):
        if arr[i-1] < arr[i]:
            continue

        unsorted = arr[i]
        j = i-1

        while j >=0 and unsorted < arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = unsorted

def insertionSortDesc(arr:list[int]) -> None:
    n = len(arr)

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            continue

        unsorted = arr[i]
        j = i-1

        while j >=0 and unsorted > arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = unsorted

arr1 = [5,7,8,4,1,6,9,2]
arr2 = [5,7,8,4,1,6,9,2]
insertionSort(arr1)
insertionSortDesc(arr2)
print(arr1)
print(arr2)
