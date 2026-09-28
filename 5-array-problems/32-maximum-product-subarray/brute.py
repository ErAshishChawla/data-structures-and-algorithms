def maxProducSubarray(arr:list[int]) -> int:
    n = len(arr)
    
    max_prod = float("-Inf")

    for i in range(0,n):
        curr_prod = arr[i]
        for j in range(i,n):
            if i != j:
                curr_prod = curr_prod * arr[j]

            max_prod = max(max_prod, curr_prod)

    return max_prod

arr = [-2,3]
print(maxProducSubarray(arr))
