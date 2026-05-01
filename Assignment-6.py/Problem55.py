def sortByFrequency(s):
    from collections import Counter
    
    freq = Counter(s)
    
    sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
    
    result = ''
    
    for ch, count in sorted_chars:
        result += ch * count
    
    return result