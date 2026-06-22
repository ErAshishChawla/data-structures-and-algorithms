def setMatrixZero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rowsAffected = set()
    colsAffected = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rowsAffected.add(i)
                colsAffected.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in rowsAffected or j in colsAffected:
                matrix[i][j] = 0

def printMatrix(matrix):
    rows= len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end = " ")
        print()

matrix = [[0,1,2,0], [3,4,0,2], [1,3,1,5]]
print("Actual Matrix:")
printMatrix(matrix)
setMatrixZero(matrix)
print("Result Matrix:")
printMatrix(matrix)
            
