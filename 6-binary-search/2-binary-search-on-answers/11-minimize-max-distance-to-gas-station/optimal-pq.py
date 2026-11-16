import heapq

def minMaxDistance(arr:list[int],k:int) -> float:
    n = len(arr)
    section_placement = [0 for _ in range(0, n-1)]
    pq = []

    # Initial Setup
    for i in range(0, n-1):
        dist = (arr[i+1] - arr[i]) / (section_placement[i] + 1)
        heapq.heappush(pq, [-dist, dist, i])
    
    for i in range(0, k):
        _, sec_dist, idx = heapq.heappop(pq)
        section_placement[idx] += 1

        dist=(arr[idx + 1] - arr[idx]) / (section_placement[idx] + 1)
        heapq.heappush(pq, [-dist, dist, idx])
        
    return -pq[0][0]

print(minMaxDistance([1, 13, 17, 23], 5))