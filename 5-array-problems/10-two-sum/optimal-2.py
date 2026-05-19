def twoSum(arr, target):
    n = len(arr)
    idx_map = dict()

    for i in range(n):
        val = arr[i]
        complement = target - val

        if complement in idx_map:
            return [idx_map[complement], i]
        
        idx_map[val] = i

nums = [2,5,5,11]
target = 10

print(twoSum(nums, target))
