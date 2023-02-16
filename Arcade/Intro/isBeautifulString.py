def solution(inputString):
    
    '''
    alphabet = string.ascii_lowercase
    for i in alphabet:
        temp = [inputString.count(i)]
    print(temp)
    return temp[::-1] == sorted(temp)
    '''
    
    
    r = [inputString.count(i) for i in string.ascii_lowercase]
    
    print(r)
    print(sorted(r))
    print(r[::-1])
    return r[::-1] == sorted(r)
