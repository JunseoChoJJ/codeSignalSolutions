def solution(symbol):
    
    if symbol.isdigit():
        symbol = int(symbol)
        if symbol % 2 == 0:
            return "even"
        else:
            return "odd"
    else:
        return "not a digit"
    
    
    '''
    best voted solution
    
    return "not a digit" if not s.isdigit() else "odd" if int(s)%2 else "even"
    
    
    '''
