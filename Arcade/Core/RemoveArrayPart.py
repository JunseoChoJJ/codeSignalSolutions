def solution(inputArray, l, r):
    
    return inputArray[:l] + inputArray[r+1:]
    
    '''
    del inputArray[l:r+1]
    
    return inputArray
    '''
