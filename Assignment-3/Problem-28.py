def search_matrix(matrix, target):
    if not matrix:
        return False
    n, m = len(matrix), len(matrix[0])
    l, r = 0, n*m - 1

    while l <= r:
        mid = (l + r) // 2
        val = matrix[mid//m][mid % m]
        if val == target:
            return True
        elif val < target:
            l = mid + 1
        else:
            r = mid - 1
    return False