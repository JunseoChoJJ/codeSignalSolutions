def solution(n, firstNumber):
    midpoint = n // 2
    
    if firstNumber < midpoint:
        return midpoint + firstNumber
    else:
        return firstNumber - midpoint
