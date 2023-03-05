def solution(number):
    #gameplan : 
    number = ord(number)
    one = number - 65
    num = one // 2 + 1
    
    ans = []
    
    for i in range(num):
        new = ""
        another = one - i
        first = i + 65
        second = another + 65
        new += chr(first) + " + " + chr(second)
        ans.append(new)
        
    return ans
    
    '''
    bestvoted solution
    
    arr = []
    for i in range(0, (ord(number)-65)//2 + 1):
        arr.append(chr(65+i)+' + '+chr(ord(number)-i))
    return arr
    
    feedback : same logic but it is more neat
    '''
