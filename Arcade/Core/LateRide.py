def solution(n):
    if n == 0:
        return 0

    minute = str(n // 60)
    second = str(n % 60)
    
    if len(minute) == 1:
        minute = "0" + minute
    if len(minute) == 0:
        minute = "00"
    if len(second) == 1:
        second = "0" + second
    if len(second) == 0:
        second == "00"
    ans = int(minute[0]) + int(minute[1]) + int(second[0]) + int(second[1])
    return ans    
    
    '''
    best voted solution    
    return sum(map(int, str(n // 60 * 100 + n % 60)))
    
    I need to learn how to use map function
    
    '''
