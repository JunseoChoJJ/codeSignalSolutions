def solution(n):
    length = len(str(n)) // 2
    
    sum1 = 0
    sum2 = 0
    
    for i in range(0, length):
        sum1 += int(str(n)[i])
    
    for j in range(length, len(str(n))):
        sum2 += int(str(n)[j])
    if sum1 == sum2:
        return True
    else:
        return False
