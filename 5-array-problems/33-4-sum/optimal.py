def fourSum(arr:list[int], target:int) -> list[list[int]]:
    n = len(arr)
    arr.sort()
    result = []

    if n < 4:
        return result

    for i in range(0, n):
        if i > 0 and arr[i-1] == arr[i]:
            continue

        for j in range(i+1, n):
            if j > i+1 and arr[j-1] == arr[j]:
                continue

            k = j+1
            l = n-1

            while k<l:
                curr_sum = arr[i] + arr[j] + arr[k] + arr[l]
                if curr_sum < target:
                    k+=1
                elif curr_sum > target:
                    l -=1
                else:
                    result.append([arr[i], arr[j], arr[k], arr[l]])
                    k+=1
                    l-=1

                    while k < n and arr[k-1] == arr[k]:
                        k+=1
                    while l > j and arr[l+1] == arr[l]:
                        l-=1

    return result

nums = [1,0,-1,0,-2,2]
target = 0

print(fourSum(nums, target))