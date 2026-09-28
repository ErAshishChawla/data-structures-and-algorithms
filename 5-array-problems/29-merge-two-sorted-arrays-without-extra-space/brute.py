def merge(arr1:list[int], arr2:list[int]):
    n = len(arr1)
    m = len(arr2)
    
    for i in range(0,n):
        if arr1[i]<=arr2[0]:
            continue
        else:
            temp = arr1[i]
            arr1[i] = arr2[0]

            j = 1
            while j < m:
                if arr2[j] < temp:
                    arr2[j-1] = arr2[j]
                    j+=1
                else:
                    break

            arr2[j-1] = temp

    return

arr1 = [10]
arr2 = [1,2,3]
merge(arr1, arr2)

print(arr1)
print(arr2)