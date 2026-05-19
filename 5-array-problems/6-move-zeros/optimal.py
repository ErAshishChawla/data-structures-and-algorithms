def moveZeros(arr):
    n = len(arr)

    if n <= 1:
        return

    i = 0

    for j in range(1, n):
        if arr[i] != 0:
            i += 1
            continue

        if arr[j] == 0:
            continue

        arr[i], arr[j] = arr[j], arr[i]
        i+=1 

arr = [0, 0, 0, 1, 2, 0, 0, 5,6, 0, 7]
moveZeros(arr)
print(arr)