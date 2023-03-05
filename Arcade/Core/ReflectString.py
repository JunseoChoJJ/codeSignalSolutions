def solution(inputString):
    
    majicNum = 97 + 122
    ans = ""
    for i in inputString:
        n = ord(i)
        reflect = majicNum - n
        alphabet = chr(reflect)
        ans += alphabet
    return ans
