def threeSum(arr):
    n = len(arr)
    sorted_arr = sorted(arr)

    result = []

    for i in range(0,n):
        if i!=0 and sorted_arr[i] == sorted_arr[i-1]:
            continue

        j = i+1
        k = n-1

        while j < k:
            total = sorted_arr[i] + sorted_arr[j] + sorted_arr[k]
            if total < 0:
                j += 1
            elif total > 0:
                k-=1
            else:
                triplet = [sorted_arr[i], sorted_arr[j], sorted_arr[k]]
                result.append(triplet)
                j += 1
                k -= 1

                while j < k and sorted_arr[j] == sorted_arr[j-1]:
                    j +=1 
                while j < k and sorted_arr[k] == sorted_arr[k+1]:
                    k -=1
        
    return result