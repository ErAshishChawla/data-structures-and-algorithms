def mergeArr(arr, left, mid, right):

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid+1:right+1]

    i = 0
    j = 0
    n = len(left_arr)
    m = len(right_arr)

    result = []

    while i < n and j < m:
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i+=1

        else:
            result.append(right_arr[j])
            j+=1

    for x in range(i, n):
        result.append(left_arr[x])

    for y in range(j, m):
        result.append(right_arr[y])

    for z in range(left, right+1):
        arr[z] = result[z-left]

    return arr

def mergeSort(arr):
    n = len(arr)
    size = 1

    while size < n:
        start = 0 
        while start < n:
            mid = start + size - 1
            end = min(start + (2* size) - 1, n-1)

            if mid >=n-1:
                break

            mergeArr(arr, start, mid, end)
            start = end + 1

        size = 2*size

arr = [4,6,1,2,6,7,2,1,0]
mergeSort(arr)
print(arr)


