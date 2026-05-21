def majorityElement(arr):
    n = len(arr)
    candidate = None
    votes = 0

    for val in arr:
        if votes == 0:
            candidate = val
            votes = 1
            continue

        if val == candidate:
            votes += 1
        else:
            votes -= 1

    count = 0
    for val in arr:
        if val == candidate:
            count += 1

    return candidate if count > n//2 else None

arr = [3,2,3]
print(majorityElement(arr))