def mergeIntervals(intervals:list[list[int]]) -> list[list[int]]:
    arr = sorted(intervals, key=lambda x: x[0])

    n = len(arr)
    if n <=0:
        return []
    
    result = [arr[0]]
    for j in range(1, n):
        interval = arr[j]

        start1 = result[-1][0]
        end1 = result[-1][1]

        start2 = interval[0]
        end2 = interval[1]

        if (start1 <= start2 and start2<=end1) or (start2<=start1 and start1<=end2):
            result[-1][0] = min(start1, start2)
            result[-1][1] = max(end1, end2)
        else:
            result.append(interval)

    return result

arr1 = [[1,3],[2,6],[8,10],[15,18]]
arr2 = [[1,4],[4,5]]
arr3=[[4,7],[1,4]]
arr4=[[2,3],[4,5],[6,7],[8,9],[1,10]]
print(mergeIntervals(arr1))
print(mergeIntervals(arr2))
print(mergeIntervals(arr3))
print(mergeIntervals(arr4))