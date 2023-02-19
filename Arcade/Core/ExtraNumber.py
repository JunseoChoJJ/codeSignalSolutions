def solution(a, b, c):
    
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a
   
   
    '''
    best voted solution
    
    return a^b^c
    XOR	Sets each bit to 1 if only one of two bits is 1
    '''
