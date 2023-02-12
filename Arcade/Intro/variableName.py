def solution(name):
    
    
    
    # first check string's first value if it is number or not
    if name[0].isdigit():
        
        return False
    
    # if check letter and number and underscore return true else return false
    x = True
    for a in name:
        if a.isalpha() or a.isdigit():
            continue
        elif a == "_":
            continue
        else:
            return False
    return x
    
    # I just put return True inside if and elif that'why my for loop just checked my first element
    
    '''
    best voted solution:
        return name.isidentifier()
        
        진짜 python method는 마법이다;;; isalpha랑 isdigit만 써도 감지덕지인데 ㅋㅋㅋㅋ
