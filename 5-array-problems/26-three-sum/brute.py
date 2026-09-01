def threeSum(arr: list[int]):
    n = len(arr)

    result_set = set()

    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet_arr = [arr[i], arr[j], arr[k]]
                    triplet_arr.sort()
                    result_set.add(tuple(triplet_arr))

    return [list(t) for t in result_set]


arr = [-1,0,1,2,-1,-4]
print(threeSum(arr))

