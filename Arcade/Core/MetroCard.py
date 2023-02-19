def solution(lastNumberOfDays):
    
    ans = [28,30,31]
    ans2 = [31]
    if lastNumberOfDays == 30:
        return ans2
    if lastNumberOfDays == 31:
        return ans
    if lastNumberOfDays == 28:
        return ans2
