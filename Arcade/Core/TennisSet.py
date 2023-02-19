def solution(score1, score2):
    if score1 > 7 or score2 > 7:
        return False
    if score1 == 7:
        if score2 == 6 or score2 == 5:
            return True
        else:
            return False
    if score2 == 7:
        if score1 == 5 or score1 == 6:
            return True
        else:
            return False
    if score1 == 6:
        if score2 <= 4:
            return True
        else:
            return False 
    if score2 == 6:
        if score1 <= 4:
            return True
        else:
            return False 
            
    return False
    
    '''
    
    best voted solution
    mins, maxs = (min(score1, score2), max(score1, score2))
    return (maxs == 6 and mins < 5) or (maxs == 7 and mins in (5,6))
    
    '''
