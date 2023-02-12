def solution(cell1, cell2):
    
    color = "black"
    color2 = "black"
    if ord(cell1[0]) % 2 == 1:
        if int(cell1[1]) % 2 == 1:
            color = "black"
        else:
            color = "white"
    else:
        if int(cell1[1]) % 2 == 1:
            color = "white"
        else:
            color = "black"
    if ord(cell2[0]) % 2 == 1:
        if int(cell2[1]) % 2 == 1:
            color2 = "black"
        else:
            color2 = "white"
    else:
        if int(cell2[1]) % 2 == 1:
            color2 = "white"
        else:
            color2 = "black"
            
    if color == color2:
        return True
    else:
        return False
        
'''
    best voted solution
    return (ord(cell1[0])+int(cell1[1])+ord(cell2[0])+int(cell2[1]))%2==0

'''
