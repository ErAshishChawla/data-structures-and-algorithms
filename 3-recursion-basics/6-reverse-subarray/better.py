def reverseSubarray(arr, l, r):
    while l < r:
        arr[l - 1], arr[r - 1] = arr[r - 1], arr[l-1]
        l = l+1
        r = r-1
    
arr= [1,2,3,4,5,6,7]
reverseSubarray(arr, 2,5)
print(arr)