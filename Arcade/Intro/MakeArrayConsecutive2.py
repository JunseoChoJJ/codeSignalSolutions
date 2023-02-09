def solution(statues):
    statues = sorted(statues)
    
    low = statues[0]
    high = statues[len(statues) - 1]
    
    remain = len(statues) - 2
    
    return high - remain - low - 1
