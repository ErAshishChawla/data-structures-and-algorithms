def largest(arr:list[int]) -> int:
    neg_inf = "-Inf"

    maxi = float(neg_inf)

    for val in arr:
        if val > maxi:
            maxi = val
    return maxi

arr = [1,2,3,4,5,6,7,8,9,10]
print(largest(arr))