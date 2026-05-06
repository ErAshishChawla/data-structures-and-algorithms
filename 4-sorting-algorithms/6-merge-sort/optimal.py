def mergeArr(left:list[int], right:list[int], order:str):
    n = len(left)
    m = len(right)
    result = []

    sanitized_order = order.strip().lower()

    i = 0
    j = 0

    while i < n and j < m:
        if sanitized_order == "asc":
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        else:
            if left[i] >= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

    for x in range(i, n):
        result.append(left[x])

    for y in range(j, m):
        result.append(right[y])

    return result

def mergeSort(arr:list[int], order:str):
    n = len(arr)
    if n <= 1:
        return arr

    mid  = n//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = mergeSort(left_arr, order)
    right = mergeSort(right_arr, order)

    return mergeArr(left, right, order)

arr = [4,6,1,2,6,7,2,1,0]
print(mergeSort(arr, "asc"))
print(mergeSort(arr, "desc"))

