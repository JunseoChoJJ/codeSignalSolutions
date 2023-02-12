def solution(n):
    
    # game plan: turn a single number into single digits
    # use % to figure out single digit is even or odd
    nList = [int(x) for x in str(n)]
    
    for i in range(len(nList)):
        if nList[i] % 2 != 0:
            return False
        else:
            continue
    return True
    
    
    '''
    best votes solution:
    
    return all([int(i)%2==0 for i in str(n)])
    
    what is all method?
    The all() function returns True if all items in an iterable are true, otherwise it returns False.

    If the iterable object is empty, the all() function also returns True.
    copyright for w3school
    '''
