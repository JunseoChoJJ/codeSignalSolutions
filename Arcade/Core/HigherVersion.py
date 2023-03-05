def solution(ver1, ver2):
    ver1 = list(map(int, ver1.split(".")))
    ver2 = list(map(int, ver2.split(".")))
    
    if ver1 == ver2:
        return False
    
    for i in range(len(ver1)):
        if ver1[i] > ver2[i]:
            return True
        elif ver1[i] == ver2[i]:
            continue
        else:
            return False
            
    '''
    best voted solution
    
    return list(map(int,ver1.split('.'))) > list(map(int,ver2.split('.')))
    
    
    feedback : I don't need to use for loop 
    '''
