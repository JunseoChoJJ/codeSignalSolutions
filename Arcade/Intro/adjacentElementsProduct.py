def solution(inputArray):
    maxNum = -1000
    
    for i in range(0, len(inputArray), 1):
        if((i+1) == len(inputArray)): break
        num = inputArray[i] * inputArray[i + 1]
        if (maxNum < num):
            maxNum = num
            
    return maxNum
