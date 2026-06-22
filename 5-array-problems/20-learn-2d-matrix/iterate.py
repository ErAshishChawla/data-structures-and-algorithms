def iterateMatrix(matrix: list[list[int]]):
    rows = len(matrix)

    if rows == 0:
        print("Empty matrix")
        return

    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

    return


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

iterateMatrix(matrix)
