def threeSum(arr):
    n = len(arr)

    result_set = set()

    for i in range(0, n):
        my_set = set()
        for j in range(i+1, n):
            third = -1 * (arr[i] + arr[j])
            if third in my_set:
                temp = [arr[i], arr[j], third]
                temp.sort()
                result_set.add(tuple(temp))

            my_set.add(arr[j])

    return [list(t) for t in result_set]

arr = [-1,0,1,2,-1,-4]
print(threeSum(arr))