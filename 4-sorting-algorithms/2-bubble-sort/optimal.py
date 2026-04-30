def bubbleSort(arr:list[int]) -> None:
    n = len(arr)

    for i in range(n-2, -1, -1):
        isSwap = False
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwap = True
        if not isSwap:
            break

def bubbleSortDesc(arr:list[int]) -> None:
    n = len(arr)

    for i in range(n-2, -1, -1):
        isSwap = False
        for j in range(0, i+1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwap = True
        if not isSwap:
            break





arr1 = [5,7,8,4,1,6,9,2]
arr2 = [5,7,8,4,1,6,9,2]
bubbleSort(arr1)
bubbleSortDesc(arr2)
print(arr1)
print(arr2)