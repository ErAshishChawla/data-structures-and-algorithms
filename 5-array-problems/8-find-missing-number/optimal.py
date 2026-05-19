def missingNumber(arr):
    n=len(arr)
    target = (n * (n+1))//2
    actual = sum(arr)

    return target - actual