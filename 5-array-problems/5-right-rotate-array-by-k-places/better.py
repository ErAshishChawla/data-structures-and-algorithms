def rightRotate(arr, k):
    n = len(arr)
    rotations = k % n

    if n == 0:
        return

    temp = [0] * n

    for i in range(n):
        new_index = (i+rotations) % n
        temp[new_index] = arr[i]

    arr[:] = temp

arr = [1, 2, 3, 4, 5]
rightRotate(arr, 2)
print(arr)