def rearrangeArray(arr):
    n = len(arr)
    pos = 0
    neg = 1

    ans = [0] * n

    for i in range(n):
        if arr[i] >= 0:
            ans[pos] = arr[i]
            pos += 2
        else:
            ans[neg] = arr[i]
            neg += 2

    return ans


arr = [1, -2, -3, 4, 5, -6]
print(rearrangeArray(arr))
