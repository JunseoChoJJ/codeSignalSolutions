def solution(n):
    ans = []
    
    ans.append(int(str(n)[0])) 
    ans.append(int(str(n)[1]))
    return sum(ans)
    
    
    '''
    best voted solution
    return n // 10 + n % 10
    
    I don't need to use append function I rather just use math 
    '''
