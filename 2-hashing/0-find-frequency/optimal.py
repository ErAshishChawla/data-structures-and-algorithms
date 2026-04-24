def findFrequency(arr:list[int], x:int):
    count = 0
    for num in arr:
        if num == x:
            count = count + 1
    return count



    
print(findFrequency([1,1,2,2,2,2,3,3,3,4], 2))