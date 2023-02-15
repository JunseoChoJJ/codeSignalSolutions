def solution(value1, weight1, value2, weight2, maxW):
    
    if (weight1 + weight2) <= maxW:
        return value1 + value2
    elif weight1 <= maxW:   
        if weight2 <= maxW:
            if value1 <= value2:       
                return value2
            else:
                return value1
        else:
            return value1
    elif weight2 <= maxW:
        if weight1 <= maxW:
            if value1 <= value2:
                return value2
            else:
                return value1
        else:
            return value2         
    else:
         return 0                   
      
'''
best voted solution
return max(int(w1<=W)*v1, int(w2<=W)*v2, int(w1+w2<=W)*(v1+v2))

int(w1<=W) gives you 1 or 0 < it makes sense
'''
