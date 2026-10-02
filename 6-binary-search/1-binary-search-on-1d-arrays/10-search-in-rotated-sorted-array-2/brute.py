def search(arr:list[int], target: int) -> bool:
    n = len(arr)

    for i in range(0, n):
        if arr[i] == target:
            return True

    return False
    