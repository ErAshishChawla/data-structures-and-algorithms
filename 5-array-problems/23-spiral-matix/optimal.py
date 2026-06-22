def printMatrix(matrix):
    rows= len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end = " ")
        print()

def spiralOrder(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    top_boundary = 0
    bottom_boundary = rows - 1
    left_boundary = 0
    right_boundary = cols - 1

    result = []

    while left_boundary <= right_boundary and top_boundary <= bottom_boundary:
        # Left to right values
        for i in range(left_boundary, right_boundary + 1):
            result.append(matrix[top_boundary][i])
        
        top_boundary += 1

        # top to bottom
        for i in range(top_boundary, bottom_boundary + 1):
            result.append(matrix[i][right_boundary])
        
        right_boundary-=1

        # Right to left
        if top_boundary <= bottom_boundary:
            for i in range(right_boundary, left_boundary - 1, -1):
                result.append(matrix[bottom_boundary][i])
            
            bottom_boundary -=1

        # Bottom to top
        if left_boundary <= right_boundary:
            for i in range(bottom_boundary, top_boundary - 1, -1):
                result.append(matrix[i][left_boundary])

            left_boundary += 1

    return result



matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print("Actual Matrix:")
printMatrix(matrix)
print(spiralOrder(matrix))
            