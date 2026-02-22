def row_with_max_1s(mat):
    n, m = len(mat), len(mat[0])
    max_row = -1
    max_ones = 0

    for i in range(n):
        
        l, r = 0, m-1
        first_one = m
        while l <= r:
            mid = (l + r)//2
            if mat[i][mid] == 1:
                first_one = mid
                r = mid - 1
            else:
                l = mid + 1
        ones = m - first_one
        if ones > max_ones:
            max_ones = ones
            max_row = i

    return max_row

print(row_with_max_1s([[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]))  # 2