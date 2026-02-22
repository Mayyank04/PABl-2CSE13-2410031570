def median_array(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n//2]
    else:
        return (arr[n//2 - 1] + arr[n//2]) / 2

print(median_array([90,100,78,89,67]))  
print(median_array([56,67,30,79]))      