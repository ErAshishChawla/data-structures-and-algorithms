def rightRotate(arr, k):
    n = len(arr)
    rotations = k % n
    
    if n == 0:
        return

    for _ in range(rotations):
        temp = arr[n-1]
        for i in range(n-2, -1, -1):
            arr[i+1] = arr[i]
        arr[0] = temp
    
arr = [1, 2, 3, 4, 5]
rightRotate(arr, 2)
print(arr)

