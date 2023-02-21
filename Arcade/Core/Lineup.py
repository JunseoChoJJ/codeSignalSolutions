def solution(commands):
    
    count = 0
    
    temp = []
    
    for i in range(len(commands)):
        
        if len(temp) == 0:
            if commands[i] == "A":
                count += 1
            else:
                temp.append(commands[i])
        else:
            if commands[i] == "A":
                continue
            else:
                count += 1
                temp.remove(temp[0])
    
    return count
                
        
    '''
    best voted solution
    weird = False
    total = 0
    for command in commands:
        if command == 'L' or command == 'R':
            weird = not weird
        if not weird:
            total += 1
    return total
    '''    
