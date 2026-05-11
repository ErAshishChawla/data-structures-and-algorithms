def leftRotate(arr, k):
    n = len(arr)
    rotations = k % n

    if rotations == 0:
        return

    for _ in range(rotations):
        temp = arr[0]
        for i in range(1, n):
            arr[i-1] = arr[i]
        arr[n-1] = temp

arr = [1,2,3,4,5]
leftRotate(arr,2)
print(arr)