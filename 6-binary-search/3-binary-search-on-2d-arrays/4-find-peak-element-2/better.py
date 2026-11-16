def findPeakGrid(mat:list[list[int]]) -> list[int]:
    rows = len(mat)

    if rows <= 0:
        return []

    cols = len(mat[0])

    if cols <=0:
        return []

    row = 0
    col = 0

    while row >= 0 and row < rows and col>=0 and col < cols:
        val = mat[row][col]
        top = float("-Inf")
        right = float("-Inf")
        bottom = float("-Inf")
        left = float("-Inf")

        # Lets find the actual values
        if row > 0:
            top = mat[row - 1][col]
        
        if col < cols - 1:
            right = mat[row][col + 1]
        
        if row < rows - 1:
            bottom = mat[row + 1][col]

        if col > 0:
            left = mat[row][col-1]

        if val > top and val > right and val > bottom and val > left:
            return [row, col]

        maxi = max(top, right, bottom, left)

        if top == maxi:
            row -= 1
        elif bottom == maxi:
            row += 1
        elif left == maxi:
            col -= 1
        else:
            col += 1

    return []

print(findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))
        

        