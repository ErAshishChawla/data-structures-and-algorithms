def minMaxDistance(arr:list[int], k: int) -> float:
    n = len(arr)

    # Track number of placements per section
    section_placement = [0 for i in range(0, n-1)]

    # Place each station one by one
    for _ in range(0, k):
        # First you will find the max dist section
        # The section placement and section idx are
        # one on one mapping
        max_dist = float("-Inf")
        max_idx = -1

        for i in range(0, n-1):
            # Now find dist between two sections and it
            # depends on the no of placed stations between
            # them

            # As stations are placed equally,
            # The dist per section will be as follows
            dist = (arr[i+1] -  arr[i]) / (section_placement[i] + 1)
            if dist > max_dist:
                max_dist = dist
                max_idx = i

        # Here you will have the max idx now you place
        section_placement[max_idx] = section_placement[max_idx] + 1

    # Now you have the placement data, each section how
    # many are placed, run a loop to find the lowest
    # distance between the between adjacent stations after
    # placement

    res = float("-Inf")

    for i in range(0, n-1):
        dist = (arr[i+1] - arr[i]) / (section_placement[i] + 1)
        res = max(dist, res)

    return res

print(minMaxDistance([1, 13, 17, 23], 5))
