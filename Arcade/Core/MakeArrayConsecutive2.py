def solution(statues):
    
    #gameplan 
    
    statues = sorted(statues)
    
    find = statues[len(statues) - 1] - statues[0]
    
    return find - len(statues) + 1 
