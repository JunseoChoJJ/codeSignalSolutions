def solution(votes, k):
    count = 0
    high = max(votes)
    
    if k == 0:
        if votes.count(high) > 1:
            return 0
        else:
            return 1
    
    
    for i in votes:
        if i + k > high:
            count += 1
    return count
    
    
    '''
    best voted solution:
    
    m = max(votes)
    if k == 0:
        return 1 if len([x for x in votes if x==m]) == 1 else 0
    return len([x for x in votes if x+k > m])
    
    
    '''
