def solution(n):
    
    
    
    if n < 10:
        return 0
    
    sumOfDigits = sum([int(i) for i in str(n)])
    
    return solution(sumOfDigits) + 1
    
    
    '''
    need to study again
    the solution uses recursion
    
    my answer:
    p = list(map(int, str(n)))
    
    if(len(p) == 1):
        return 0
    elif sum(p) < 10:
        return 1
    else:
        while(sum(p) >= 10):
            if(sum(p))
    '''
