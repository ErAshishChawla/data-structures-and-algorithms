def longestConsecutiveSequence(arr):
    n = len(arr)

    max_len = 0

    for i in range(n):
        curr_len = 1
        next_num = arr[i] + 1

        while True:
            flag = 0
            for j in range(n):
                if arr[j] == next_num:
                    curr_len += 1
                    flag = 1
                    break

            if flag == 1:
                next_num += 1
            else:
                break

        max_len = max(max_len, curr_len)

    return max_len


arr1 = [1,0,1,2]
arr2 = [100, 4, 200, 2, 15, 16, 1, 1, 1, 3]
print(longestConsecutiveSequence(arr1))
print(longestConsecutiveSequence(arr2))
