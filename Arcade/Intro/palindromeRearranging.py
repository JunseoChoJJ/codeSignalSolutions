def solution(inputString):
    
    #game plan : look at the pattern, there is difference between odds and even, I will divide into two using if, else
    # if even, each character should be even if odd, one character should be odd others are even
    #if len(a) % 2 == 0:
        
    l = list(inputString)
    
    chars = set(l)
    
    counts = sum([l.count(x) % 2 for x in chars])
        
        
    return counts <= 1
