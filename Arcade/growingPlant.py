def solution(upSpeed, downSpeed, desiredHeight):
    
    # let's make a while loop
    
    count = 0
    height = 0
    
    while(True):
        height += upSpeed
        count += 1
        if(height >= desiredHeight):
            break
        height -= downSpeed
        
    return count

'''
best voted solution
if desiredHeight <= upSpeed:
        return 1
    return math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed) + 1)

this would be better in time complexity perspective
what is math.ceil()?
Smallest integer not less than x.

math.floor(x)
largest integer not greater than x.
'''
