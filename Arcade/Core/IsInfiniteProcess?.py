def solution(a, b):
    # gameplan : find the pattern when does infinite loop happens
    # b-a should be odd to get infinite loop
    
    if a > b:
        return True
    if a == 0:
        return abs(b-a) % 2 == 1
    else:
        return abs(b-a) % 2 == 1 
    
    
    '''
    best voted solution
    
    return (a+b)%2 != 0 or (a > b)
    '''
