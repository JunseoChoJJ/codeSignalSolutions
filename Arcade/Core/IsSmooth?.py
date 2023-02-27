def solution(arr):
    #game plan divide into odd and even
    
    if len(arr) % 2 == 0:
        middle = len(arr) // 2
        print(middle)
        if arr[0] == arr[len(arr) - 1] and arr[0] == arr[middle - 1] + arr[middle]:
            return True
            print("hi`")
        else:
            return False
            print("bye")
    else:
        middle = len(arr) // 2 
        
        if arr[0] == arr[middle] and arr[0] == arr[len(arr) - 1]:
            return True
        else:
            return False
