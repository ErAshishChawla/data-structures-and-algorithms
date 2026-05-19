def twoSum(arr, target):
    n = len(arr)
    idx_map = dict()

    for idx in range(n):
        val = arr[idx]
        idx_map[val] = idx

    for i in range(n):
        one = arr[i]
        two = target - one

        if two in idx_map and idx_map[two] != i:
            return [i, idx_map[two]]

nums = [2,5,5,11]
target = 10

print(twoSum(nums, target))
