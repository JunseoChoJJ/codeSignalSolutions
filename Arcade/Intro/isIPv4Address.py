def solution(inputString):
    l = inputString.split('.')
    
    if len(l) != 4:
        return False
    for i in range(len(l)):
        if not l[i].isnumeric():
            return False
        elif (len(l[i]) > 1) and (l[i][0] == '0'):
            return False
        elif int(l[i]) not in range(256):
            return False
    return True
    
    
    '''
    string = inputString.split(".")
    
    if(len(string) != 4):
        return False    
    for i in range(0,len(string)):
        if not string[i].isdigit():
            return False 
        if (len(string[i]) > 1) and (string[i][0] == '0'):
        #if len(string[i]) == 0:
         #   return False
        if int(string[i]) > 255:
           return False
        
        
    return True
    '''
    
