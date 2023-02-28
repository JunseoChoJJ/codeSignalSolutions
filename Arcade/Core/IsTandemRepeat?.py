def solution(inputString):
    n = len(inputString)
    
    
    if inputString[0: n // 2] == inputString[n//2 :]:
        return True
    else:
        return False
