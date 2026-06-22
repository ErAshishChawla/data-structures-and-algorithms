def printMatrix(matrix):
    rows= len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end = " ")
        print()

def rotateClockwise(matrix):
    rows = len(matrix)
    cols = len(matrix)

    # Transpose in place

    for i in range(rows):
        for j in range(i+1, cols):
            if i <= j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    i = 0
    j = cols-1

    while i < j:
        for r in range(rows):
            matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
        i+=1
        j-=1

    
    
matrix = [[0,1,2], [3,4,0], [1,3,1]]
print("Actual Matrix:")
printMatrix(matrix)
rotateClockwise(matrix)
print("Result Matrix:")
printMatrix(matrix)
            
            