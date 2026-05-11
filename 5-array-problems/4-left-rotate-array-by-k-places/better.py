def leftRotate(arr, k):
    n = len(arr)
    rotations = k % n

    if n ==0:
        return

    temp = [0] * n
    for i in range(n):
        new_idx = (i - rotations) % n
        temp[new_idx] = arr[i]

    arr[:] = temp

arr = [1,2,3,4,5]
leftRotate(arr,2)
print(arr)