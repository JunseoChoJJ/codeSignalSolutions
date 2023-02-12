def solution(a):
    '''
    diffs=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)
    
    
    '''
    for i in range(0, len(a) - 1):
        diff = [abs(a[i] - a[i+1])]
        
    print(diff)    
        
    return max(diff)
    
