def solution(coins, price):
    # game plan : greedy problem
    coins.reverse()
    
    count = 0
    for i in coins:
        count += price // i
        price = price % i
    return count
    
    
    '''
    best voted solution 
    
    res = 0
    for x in reversed(coins):
        t, price = divmod(price, x)
        res += t
    return res
    
    opinion:
    I think I don't need to use for the divmod function. it takes time to search the function 
    my code is more intuitive to understand
    '''
