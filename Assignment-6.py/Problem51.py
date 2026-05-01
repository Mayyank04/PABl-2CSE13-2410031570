def min_swaps(s1, s2):
    countA = 0
    countB = 0
    
    for i in range(len(s1)):
        if s1[i] == '0' and s2[i] == '1':
            countA += 1
        elif s1[i] == '1' and s2[i] == '0':
            countB += 1
    
    if countA != countB:
        return -1
    
    return countA