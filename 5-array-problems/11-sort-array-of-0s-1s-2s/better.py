def sortArr(arr):
    n = len(arr)

    i = 0
    # First loop to sort 0s
    for j in range(i+1, n):
        if arr[i] == 0:
            i += 1
            continue

        if arr[i] != 0 and arr[j] !=0:
            continue

        arr[i], arr[j] = arr[j], arr[i]
        i+=1

    # Second loop to sort 1s
    for k in range(i+1, n):
        if arr[i] == 1:
            i+=1
            continue

        if arr[i] != 1 and arr[k] != 1:
            continue

        arr[i], arr[k] = arr[k], arr[i]
        i+=1

arr = [2,0,2,1,1,0]
sortArr(arr)
print(arr)

