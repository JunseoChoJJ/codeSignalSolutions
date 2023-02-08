def solution(inputString):
    
    output = ""
    
    
    for i in range(len(inputString) - 1, -1, -1):
        output += inputString[i]
    
    
    if output == inputString:
        return True
    else:
        return False
