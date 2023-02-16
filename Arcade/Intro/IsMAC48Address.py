def solution(inputString):

    # game plan : split into 6groups and check if it is valid or not
    # need to try again
    try:
        all = inputString.split('-')
        if len(all) !=6:
            return False
        for s in all:
            if len(s) != 2:
                return False
            print(int(s,16))
        return True
    except:
        return False
    
    
    
    
    
    '''
    mac = inputString.split("-")
    if len(mac) != 6:
        return False
    res = ""
    #how can I split digit and letter
    for i in mac:
        res += re.split(('\d'), mac[i])
        
    '''
