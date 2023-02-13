def solution(deposit, rate, threshold):
    
    
    return math.ceil(math.log(threshold/deposit, 1+rate/100))
    
    
    
    
    '''
    year = 0
    
    while True:
        if deposit >= threshold:
            break
        year += 1
        deposit = deposit + deposit * rate // 100
    
    return year
    
    I got execution time error
    
    why?
    '''
