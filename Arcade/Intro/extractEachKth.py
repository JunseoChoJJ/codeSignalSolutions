def solution(inputArray, k):
# you need to make difference between num and k
    num = k - 1
    ans = []
    for i in range(len(inputArray)):
        
        if i == num:
            num += k
        else:
            ans.append(inputArray[i])
            
    return ans

'''
best voted solution:
del inputArray[k-1::k]
    return inputArray
what is del?
 del[a : b] :- This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
 The last k is for increment like for loop last argument

'''
