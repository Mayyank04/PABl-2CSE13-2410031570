def min_swaps(arr, k):
    n = len(arr)
    good = sum(1 for x in arr if x <= k)
    if good == 0:
        return 0

    bad = sum(1 for i in range(good) if arr[i] > k)
    ans = bad

    for i in range(0, n - good):
        if arr[i] > k:
            bad -= 1
        if arr[i + good] > k:
            bad += 1
        ans = min(ans, bad)

    return ans

print(min_swaps([2,1,5,6,3], 3))  # 1