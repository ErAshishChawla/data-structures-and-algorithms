def fourSum(arr:list[int], target:int) -> list[list[int]]:
    n = len(arr)
    result:set[tuple[int, int, int]] = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        quad_arr = [arr[i], arr[j], arr[k], arr[l]]
                        quad_arr.sort()
                        result.add(tuple(quad_arr))
    return [list(t) for t in result]
    
nums = [1,0,-1,0,-2,2]
target = 0

print(fourSum(nums, target))