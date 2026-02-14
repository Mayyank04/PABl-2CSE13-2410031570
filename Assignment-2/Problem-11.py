import heapq

def kth_smallest(arr, k):
    max_heap = []

    for num in arr:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return -max_heap[0]

print(kth_smallest([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 4))
print(kth_smallest([7, 10, 4, 3, 20, 15], 3))               