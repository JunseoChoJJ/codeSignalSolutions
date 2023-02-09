def solution(inputArray):
    
    big = len(inputArray[0])
    
    ans = []
    if len(inputArray) == 1:
        return inputArray
    for i in range(0, len(inputArray)):
        if big <= len(inputArray[i]):
            big = len(inputArray[i])
            
    

    
    for j in range(0, len(inputArray)):
        if big == len(inputArray[j]):
            ans.append(inputArray[j])
            
    return ans
