def diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i == j:
                print(matrix[i][j], end=" ")
            elif i + j == rows - 1:
                print(matrix[i][j], end = " ")
            else:
                print("*", end = " ")
        print()

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
diagonal(matrix)