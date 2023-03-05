def solution(message):
    # gameplan: 
    
    prev_number = 0
    ans = ""
    for char in message:
        
        cur_number = ord(char) - ord('a') + 26
        print(cur_number)
        orig_char = chr((cur_number - prev_number) % 26 + ord('a'))
        print(orig_char)
        ans += orig_char
        prev_number = ord(char) - ord('a')
    return ans
