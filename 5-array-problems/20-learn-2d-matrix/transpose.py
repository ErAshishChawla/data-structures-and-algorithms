def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # We need columns for number of rows so we create columns by [0]*rows and then repeat it cols times
    transpose = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose

def printMatrix(matrix):
    rows= len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end = " ")
        print()


matrix = [[5,9,1],[2,3,7]]
print("Actual Matrix:")
printMatrix(matrix)
print("Transposed Matrix:")
printMatrix(transpose(matrix))