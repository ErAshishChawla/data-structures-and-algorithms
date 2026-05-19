def mergeArr(left, right):
    n = len(left)
    m = len(right)

    res = []

    i = 0
    j = 0

    while i < n and j < m:
        append_element = None
        if left[i] < right[j]:
            append_element = left[i]
            i+=1
        elif left[i] == right[j]:
            append_element=left[i]
            i+=1
            j+=1
        else:
            append_element = right[j]
            j+=1

        if len(res) == 0 or res[-1] != append_element:
            res.append(append_element)

    for x in range(i, n):
        if res[-1] != left[x]:
            res.append(left[x])

    for y in range(j, m):
        if res[-1] != right[y]:
            res.append(right[y])

    return res

print(mergeArr([1,2,3,4,5], [1,2,3]))
print(mergeArr([1,2,3,4,5], [1,2,3,6,7]))
print(mergeArr([2,2,3,4,5], [1,1,2,3,4]))
print(mergeArr([1,1,1,1,1], [2,2,2,2,2]))

            

