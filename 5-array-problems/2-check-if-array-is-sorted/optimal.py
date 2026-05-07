def isSorted(arr:list[int]) -> bool:
    n = len(arr)

    if len(arr) <= 1:
        return True

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    
    return True

arr1 = [1,2,3,4,5,6,7,8,9,10]
print(isSorted(arr1))

arr2 = [1,2,3,4,5,6,7,8,9,10,3,4]
print(isSorted(arr2))