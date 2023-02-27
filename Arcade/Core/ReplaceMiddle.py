def solution(arr):
    if len(arr) % 2 == 0:
        middle = len(arr) // 2
        print(middle)
        mid = [arr[middle - 1] + arr[middle]]
            
        return arr[:middle-1] + mid + arr[middle+1:]
    else:
        return arr
