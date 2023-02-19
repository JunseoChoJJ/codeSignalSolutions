def solution(min1, min2_10, min11, s):
    count = 0
    
    
    if s < min1:
        return count
    else:
        s -= min1
        count+=1
    
    
    
    while s > 0:
        if count < 10:
            if min2_10 > s:
                break
            else:
                s -= min2_10
                count += 1
                print("hi")
        else:
            if min11 > s:
                break
            else:
                s -= min11
                count += 1
    return count
            
    ''' 
    best voted solution
    if s<min1:
        return 0
    elif s>=min1 and s<=min1+9*min2_10:
        return 1+(s-min1)//min2_10
    return 10+(s-min1-9*min2_10)//min11
    
    didn't use for loop and while loop
    
    '''
