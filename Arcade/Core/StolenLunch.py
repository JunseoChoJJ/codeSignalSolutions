def solution(note):
    
    
    new = ""
    for i in note:
        if i.isdigit():
            num = 97+ int(i)
            char = chr(num)
            new += char
        elif i == "a" or i == "b" or i == "c" or i == "d" or i == "e" or i == "f" or i == "g" or i == "h" or i == "i" or i == "j":
            num = ord(i)
            
            char = num - 97
            new += str(char)
        else:
            new += i
    return new
    
    '''
    best voted solution
    D = '0123456789'
    L = 'abcdefghij'
    return note.translate(str.maketrans(D + L, L + D))
    
    '''
