def pascalTriangle(n):
    if n <= 0:
        return []

    result = []

    for i in range(0, n):
        m = i+1
        curr = [1] * m
        if i > 1:
            prev = result[i-1]
            for j in range(1, m // 2 + 1):
                curr[j] = prev[j] + prev[j-1]
                curr[m-j-1] = curr[j]
        result.append(curr)
    
    return result

print(pascalTriangle(7))
