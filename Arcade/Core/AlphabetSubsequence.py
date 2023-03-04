def solution(s):
    
    
    if len(set(s)) != len(s):
        print("hi")
        return False
    s = list(s)
    
    if sorted(s) != s:
        return False
    return True
    
    '''
    best voted solution
    return "".join(sorted(s)) == s and len(set(s)) == len(s)
    '''
