def searchMatrix(arr:list[list[int]], target:int) -> bool:
    rows = len(arr)

    if rows <= 0:
        return False

    cols = len(arr[0])

    row = 0
    col = cols - 1

    while row < rows and col > -1:
        curr = arr[row][col]

        if curr == target:
            return True

        if curr > target:
            col -= 1
        else:
            row += 1

    return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix(matrix, target))