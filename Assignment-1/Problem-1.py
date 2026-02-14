def reverse_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


arr = [1, 4, 3, 2, 6, 5]
print(reverse_array(arr))
