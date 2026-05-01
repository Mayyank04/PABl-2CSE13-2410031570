def count_valid_subarrays(arr):
    n = len(arr)
    stack = []
    result = 0
    
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        if not stack:
            result += (n - i)
        else:
            result += (stack[-1] - i)
        
        stack.append(i)
    
    return result