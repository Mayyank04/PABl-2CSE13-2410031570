def solve(n, m, matrix, queries):
    prefix = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            prefix[i][j] = matrix[i][j]
            
            if i > 0:
                prefix[i][j] += prefix[i-1][j]
            if j > 0:
                prefix[i][j] += prefix[i][j-1]
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i-1][j-1]
    
    result = []
    
    for r1, c1, r2, c2 in queries:
        ans = prefix[r2][c2]
        
        if r1 > 0:
            ans -= prefix[r1-1][c2]
        if c1 > 0:
            ans -= prefix[r2][c1-1]
        if r1 > 0 and c1 > 0:
            ans += prefix[r1-1][c1-1]
        
        result.append(ans)
    
    return result


# Example
n, m = 3, 3
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

queries = [
    [0,0,2,2],
    [1,0,2,1]
]

print(solve(n, m, matrix, queries))