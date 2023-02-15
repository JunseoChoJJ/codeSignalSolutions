def solution(inputString):
    ans = ""
    
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            ans += inputString[i]
        else:
            break
    return ans
    
    '''
    best voted solution
    return re.findall('^\d*',inputString)[0]
    
    what is re.findall()?
    
    '''
