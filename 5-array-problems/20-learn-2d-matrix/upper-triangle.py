def upperTriangle(matrix: list[list[int]]):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if j < i:
                print("*", end = " ")
            else:
                print(matrix[i][j], end = " ")
        print()

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
upperTriangle(matrix)


    