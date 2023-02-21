def solution(n):
    
    k = 1
    ans = 1
    
    while True:
    
        if n <= ans:
            return ans
            
        k += 1
        ans *= k
    
    '''
    best voted solution
    f=i=1
    while f<n:
        f*=i
        i+=1
    return f
    
    my condition is different and would it be affect?
    '''
