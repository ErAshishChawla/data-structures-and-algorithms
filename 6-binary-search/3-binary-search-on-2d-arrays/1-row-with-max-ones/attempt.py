def searchMatrix(matrix: list[list[int]]) -> int:
    rows = len(matrix)
    if rows<=0:
        return -1
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    idx = -1

    while row < rows and col > -1:
        curr = matrix[row][col]

        if curr == 0:
            row += 1
        else:
            idx = row
            col -= 1

    return idx

