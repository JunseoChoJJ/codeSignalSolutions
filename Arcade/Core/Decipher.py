def solution(cipher):
    # gameplan : 97 <= chr <= 122 how can I split after that is so easy
    
    ans = ""
    num = ""
    for i in cipher:
        num += i
        if int(num) >= 97:
            new = int(num)
            ans += chr(new)
            num = ""
    
    return ans 


'''
bestvoted solution
import re
def solution(cipher):
    t = re.findall(r'1?\d\d', cipher)
    return "".join(chr(int(i)) for i in t)
'''
