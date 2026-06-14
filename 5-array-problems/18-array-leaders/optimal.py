def reverse(arr):
    n = len(arr)

    i = 0
    j = n-1

    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    
    return



def arrayLeaders(arr:list[int]):
    leaders = []
    n = len(arr)

    curr_max = float("-Inf")

    for i in range(n-1, -1, -1):
        if arr[i] >= curr_max:
            leaders.append(arr[i])
            curr_max = arr[i]

    reverse(leaders)

    return leaders

arr = [16, 17, 4, 3, 5, 2]
print(arrayLeaders(arr))

