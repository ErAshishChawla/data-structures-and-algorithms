from typing import List
def majorityElement(arr:List[int]) -> List[int]:
    n = len(arr)
    cnt1 = 0
    ele1 = float("Inf")

    cnt2 = 0
    ele2 = float("Inf")

    limit = n // 3

    for i in range(0,n):
        if cnt1 == 0 and arr[i] != ele2:
            cnt1 = 1
            ele1 = arr[i]
        elif cnt2 == 0 and arr[i] != ele1:
            cnt2 = 1
            ele2 = arr[i]
        elif arr[i] == ele1:
            cnt1 += 1
        elif arr[i] == ele2:
            cnt2 += 1
        else:
            cnt1 -=1 
            cnt2 -=1
    
    result = []

    cnt1 = 0
    cnt2 = 0

    for i in range(0,n):
        if arr[i] == ele1:
            cnt1 += 1
        elif arr[i] == ele2:
            cnt2 += 1

    if cnt1 > limit:
        result.append(ele1)
    
    if cnt2 > limit:
        result.append(ele2)

    return result
        

    