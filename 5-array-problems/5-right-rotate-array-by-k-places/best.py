def rightRotate(arr, k):
    n = len(arr)
    rotations = k % n

    if n == 0:
        return 

    def reverse(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    
    reverse(arr, 0, n-1)
    reverse(arr, 0, rotations-1)
    reverse(arr, rotations, n-1)

arr = [1,2,3,4,5]
rightRotate(arr, 2)
print(arr)