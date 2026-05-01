def electionWinner(arr):
    from collections import Counter
    
    freq = Counter(arr)
    
    max_votes = 0
    winner = ""
    
    for name in sorted(freq.keys()):
        if freq[name] > max_votes:
            max_votes = freq[name]
            winner = name
    
    return [winner, str(max_votes)]