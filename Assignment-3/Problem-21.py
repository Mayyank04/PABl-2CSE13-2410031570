def chocolate_distribution(arr, m):
    if m == 0 or m > len(arr):
        return 0
    arr.sort()
    ans = float('inf')
    for i in range(len(arr) - m + 1):
        ans = min(ans, arr[i+m-1] - arr[i])
    return ans

print(chocolate_distribution([3,4,1,9,56,7,9,12], 5))  # 6