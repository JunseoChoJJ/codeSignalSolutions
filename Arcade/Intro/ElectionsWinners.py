def solution(votes, k):
    
    new = []
    
    big = max(votes) 
    count = 0
    count2 = 0
        
    for i in range(len(votes)):
        if votes[i] == big:
            count2 += 1
        new.append(votes[i] + k)
        if new[i] > big:
            count += 1
    
    if k == 0:
        if count2 > 1:
            return 0
        else:
            return 1
    else:
        return count
    
'''
best voted solution
 m = max(v)
    
return int(v.count(m) == 1) if k == 0 else len([n for n in v if m < n + k])

aha count method
'''
