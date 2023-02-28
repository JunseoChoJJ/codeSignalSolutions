def solution(startTag):
    star = startTag.split()
    
    start = star[0]
    start = start[1:]
    
    
    if len(star) == 1:
        return "</" + start
    else:
        return "</" + start + ">"    
    
    '''
    best voted solution
    
    return "</" + startTag[1:startTag.find(" ")] + ">"
    '''
