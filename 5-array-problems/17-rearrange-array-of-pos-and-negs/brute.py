def rearrangeArr(arr):
    n = len(arr)
    pos = []
    neg = []

    for i in range(n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    
    for j in range(0, n//2):
        arr[2*j] = pos[j]
        arr[2 *j+1] = neg[j]

    return arr

arr = [1, -2, -3, 4, 5, -6]
print(rearrangeArr(arr))

    