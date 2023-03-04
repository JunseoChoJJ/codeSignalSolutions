def solution(inputArray):
    
    # count the number
    num = 0 
    
    for i in inputArray:
        if num < len(i):
            num = len(i)
    ans = []
    for i in inputArray:
        if len(i) == num:
           ans.append(i) 
           
    return ans
    
    '''
    best voted solution
    return [x for x in inputArray if len(x)==max(map(len,inputArray))]
    
    '''
