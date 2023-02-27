def solution(arr):
    if len(arr) == 0:
        return arr
    
    temp = []
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    
    return arr
    
    '''
    best voted solution
    
    if len(arr) > 0 : arr[0], arr[-1] = arr[-1], arr[0]
    
    return arr
    
    '''
