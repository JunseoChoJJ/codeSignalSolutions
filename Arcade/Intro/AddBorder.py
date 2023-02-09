def solution(picture):
    
# try again

    r = ['*'*(len(picture[0])+2)]
    print(r)
    for i in picture:
        r.append('*' + i + '*')

    r.append(r[0])

    
    
    return r
