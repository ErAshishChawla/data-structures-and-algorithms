def reverseSubarray(arr,l,r):
    if l >=r:
        return

    # Swap l and r
    arr[l-1], arr[r-1] = arr[r-1], arr[l-1]

    reverseSubarray(arr, l + 1, r - 1)

arr= [1,2,3,4,5,6,7]
reverseSubarray(arr, 2,5)
print(arr)