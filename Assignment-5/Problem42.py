def solve(n, m, a, queries):
    results = []
    
    for R, C in queries:
        R -= 1
        C -= 1
        
        total = 0
        
        min_val = float('inf')
        for i in range(0, R):
            for j in range(0, C):
                min_val = min(min_val, a[i][j])
        if min_val != float('inf'):
            total += min_val
        
        min_val = float('inf')
        for i in range(0, R):
            for j in range(C+1, m):
                min_val = min(min_val, a[i][j])
        if min_val != float('inf'):
            total += min_val
        
        min_val = float('inf')
        for i in range(R+1, n):
            for j in range(0, C):
                min_val = min(min_val, a[i][j])
        if min_val != float('inf'):
            total += min_val
        
        min_val = float('inf')
        for i in range(R+1, n):
            for j in range(C+1, m):
                min_val = min(min_val, a[i][j])
        if min_val != float('inf'):
            total += min_val
        
        results.append(total)
    
    return results


# Example
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

queries = [(2,2)]
print(solve(3,3,a,queries))