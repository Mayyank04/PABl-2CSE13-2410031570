def min_people(arr):
    n = len(arr)
    intervals = []
    
    for i in range(n):
        if arr[i] != -1:
            start = max(0, i - arr[i])
            end = min(n - 1, i + arr[i])
            intervals.append((start, end))
    
    intervals.sort()
    
    count = 0
    i = 0
    current_end = 0
    max_reach = 0
    
    while current_end < n:
        found = False
        
        while i < len(intervals) and intervals[i][0] <= current_end:
            max_reach = max(max_reach, intervals[i][1] + 1)
            i += 1
            found = True
        
        if not found:
            return -1
        
        count += 1
        current_end = max_reach
    
    return count