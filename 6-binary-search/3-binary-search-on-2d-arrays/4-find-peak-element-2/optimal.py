def findPeakGrid(mat:list[list[int]]) -> list[int]:
    m = len(mat)
    if m<=0:
        return []
    
    n = len(mat[0])
    if n<=0:
        return[]

    low = 0
    high = n - 1

    while low <= high:
        mid_col = (low + high) // 2

        maxi = float("-Inf")
        max_row = -1

        for i in range(0, m):
            if mat[i][mid_col] > maxi:
                maxi = mat[i][mid_col]
                max_row = i

        right = float("-Inf")
        left = float("-Inf")

        if mid_col > 0:
            left = mat[max_row][mid_col - 1]
        
        if mid_col < n-1:
            right = mat[max_row] [mid_col + 1]

        val = mat[max_row][mid_col]

        if val > left and val > right:
            return [max_row, mid_col]

        if val < left:
            high = mid_col - 1
        else:
            low = mid_col + 1

    return []

print(findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))