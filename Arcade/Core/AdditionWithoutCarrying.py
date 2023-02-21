def solution(param1, param2):
    # gameplan : for loop bigger loop using fillzero 
    
    param2_ = str(param2)
    param1_ = str(param1)
    
    if len(param1_) > len(param2_):
        param2_ = param2_.zfill(len(param1_))
    else:
        param1_ = param1_.zfill(len(param2_))
    
    ans = ""
    for i in range(len(param1_)):
        ans += str((int(param1_[i]) + int(param2_[i])) % 10)
    return int(ans)
        
    '''
    best voted solution
    result = 0
    tenPower = 1
    while param1 > 0 or param2 > 0:
        result += tenPower * ((param1 + param2) % 10)
        param1 //= 10
        param2 //= 10
        tenPower *= 10
    return result
    '''
