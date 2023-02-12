def solution(inputString):
    #increment a character
    newChar = ""
    
    for a in inputString:
        i = ord(a)
        i += 1
        
        # if char is z, you need to go back to a 
        if i > 122:
            i -= 26
        newChar += chr(i)
    return newChar
    
    '''
    best voted solution:
    return "".join(chr((ord(i)-96)%26+97) for i in inputString)    
    
    join function이 뭘까? 
    This function joins elements of a sequence and makes it a string
    '''  
