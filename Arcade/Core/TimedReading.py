def solution(maxLength, text):
#game plan: I need to figure out how to read just the word
    
    ans = []
    text += "."
    word = ""
    for i in text:
        
        if i.isalpha():
            word += i
        else:
            ans.append(word)
            word = ""
    
    count = 0
    for j in ans:
        if j.isalpha() and len(j) <= maxLength:
            count += 1
    print(ans)
    return count
    
    '''
