def fourSum(arr:list[int], target: int) -> list[list[int]]:
    n = len(arr)
    
    if n < 4:
        return []

    result = set()
    for i in range(0,n):
        for j in range(i+1, n):
            prev = set()
            for k in range(j + 1, n):
                fourth = target - (arr[i] + arr[j] + arr[k])
                if fourth in prev:
                    quad = [arr[i], arr[j], arr[k], fourth]
                    quad.sort()
                    result.add(tuple(quad))
                prev.add(arr[k])

    return [list(t) for t in result]

nums = [1,0,-1,0,-2,2]
target = 0

print(fourSum(nums, target))