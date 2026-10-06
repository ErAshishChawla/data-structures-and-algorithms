def nthRootOfM(n:int, m:int):
    res = -1

    low = 0
    high = m

    while low<=high:
        mid = (low + high) // 2
        val = mid ** n
        
        if val == m:
            res = mid
            break
        elif val > m:
            high = mid - 1
        else:
            low = mid + 1

    return res

print(nthRootOfM(4,16))