def solution(a, b, c):
    
    if a + b == c:
        return True
    if a - b == c:
        return True
    if a * b == c:
        return True
    if a / b == c:
        return True
        
    return False
    
    '''
    
    return c in (a+b,a-b,a*b,a/b)
    
    '''
