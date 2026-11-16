def canAllocatePages(arr:list[int], k:int, max_pages:int)-> bool:
    current_student = 1
    current_pages = 0

    for pages in arr:
        if current_pages + pages > max_pages:
            current_student += 1
            current_pages = pages
        else:
            current_pages += pages
    return current_student<=k


def allocateBooks(arr:list[int], k:int) -> int:
    n = len(arr)

    if n < k:
        return -1

    low = max(arr)
    high = sum(arr)

    res = -1

    while low<=high:
        mid = (low + high) // 2

        if canAllocatePages(arr, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

        
    return res