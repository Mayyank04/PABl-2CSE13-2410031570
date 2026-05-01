def previous_greater(arr):
    stack = []
    result = []
    
    for x in arr:
        while stack and stack[-1] <= x:
            stack.pop()
        
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        
        stack.append(x)
    
    return result