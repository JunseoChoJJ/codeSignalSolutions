def solution(number, width):
    length = len(str(number))
    number = str(number)
    
    if length >= width:
        return number[length-width:]
    else:
        return number.rjust(width, '0')
        
    '''
    best voted solution:
    return str(number).zfill(width)[-width:]
    
    '''
