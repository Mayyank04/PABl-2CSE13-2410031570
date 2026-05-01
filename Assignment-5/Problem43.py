import heapq

def min_operations(arr):
    total = sum(arr)
    target = total / 2
    
    heap = [-x for x in arr]
    heapq.heapify(heap)
    
    ops = 0
    
    while total > target:
        x = -heapq.heappop(heap)
        half = x / 2
        
        total -= half
        heapq.heappush(heap, -half)
        
        ops += 1
    
    return ops