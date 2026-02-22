def matrix_median(mat):
    r, c = len(mat), len(mat[0])
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)

    desired = (r*c + 1)//2

    while low < high:
        mid = (low + high)//2
        count = 0
        for row in mat:
            
            l, h = 0, c
            while l < h:
                m = (l + h)//2
                if row[m] <= mid:
                    l = m + 1
                else:
                    h = m
            count += l

        if count < desired:
            low = mid + 1
        else:
            high = mid

    return low