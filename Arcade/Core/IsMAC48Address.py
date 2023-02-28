def solution(inputString):
    # iterate and find out isdigt 
    
    if (len(inputString) != 17): return False
    x = bool(1)
    count = 0
    for i in inputString:
        if i.isdigit() or i == "-" or i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == "F":
            x = True
        else:
            return False
        if i == "-":
            count += 1
    if count != 5:
        return False
    return x
