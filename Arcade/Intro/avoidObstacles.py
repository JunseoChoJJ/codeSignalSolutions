def solution(inputArray):
    
# you need to find that is not common divisor  try again
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1
    
    
    
    '''
    arrLen = 0
    a = sorted(inputArray)
    print(a)
    j = 2
    
    possibleLen = [2]
    
    for i in range(0, len(inputArray)):
        for j in range(2, max(inputArray)):
            if a[i] <= j:
                break
            if a[i] % j != 0:
                possibleLen.append(j)
            else:
                possibleLen.remove(j)
            
    
    '''
