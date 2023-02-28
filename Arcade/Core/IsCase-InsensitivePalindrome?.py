def solution(inputString):
    inputString = inputString.lower()
    
    
    if inputString == inputString[::-1]:
        return True
    else:
        return False
