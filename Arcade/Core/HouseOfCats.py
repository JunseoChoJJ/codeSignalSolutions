def solution(legs):
    ans = []
    
    
    if legs == 2:
        ans.append(1)
        return ans
    
    if legs % 4 == 0:
        for i in range(0, legs // 2 + 1, 2):
            ans.append(i)
    else:
        for i in range(1,legs // 2 + 1, 2):
            ans.append(i)
    
    return ans
                
    '''
    best voted solution
    return list(range(legs // 2 % 2, legs // 2 + 1, 2))
    
    '''
