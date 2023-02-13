def solution(n, firstNumber):
    # n should be always even
    # find the number which is written in the radially opposite position to firstNumber
    # which is firstNumber + n/2 if firstnumber < n/2
    
    midpoint = n//2
    
    
    if midpoint > firstNumber:
        return firstNumber + midpoint
    else:
        return firstNumber - midpoint
    
''' 
best voted solution:
return (firstNumber + n/2)%n

'''
