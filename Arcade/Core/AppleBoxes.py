def solution(k):
    
    odd = 0
    even = 0
    for i in range(1,k+1):
        if i % 2 == 1:
            odd += i * i
        else:
            even += i * i
            
    return even - odd
    
    '''
    best voted solution
    return ((-1)**n)*n*(n+1)/2
    '''
