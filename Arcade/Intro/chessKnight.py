def solution(cell):
    
    
    if cell[1] == '1' or cell[1] == '8':
        if ord(cell[0]) == 97 or ord(cell[0]) == 104:
            
            return 2
        elif ord(cell[0]) == 98 or ord(cell[0]) == 103:
            
            return 3
        else:
            
            return 4 
    elif cell[1] == '2' or cell[1] == '7':
        if ord(cell[0]) == 97 or ord(cell[0]) == 104:
            
            return 3
        elif ord(cell[0]) == 98 or ord(cell[0]) == 103:
            
            return 4
            
        else:
            
            return 6
    else:
        if ord(cell[0]) == 97 or ord(cell[0]) == 104:
            
            return 4
        elif ord(cell[0]) == 98 or ord(cell[0]) == 103:
            
            return 6
        else:
            
            return 8
           
'''
best voted solution

x,y = ord(c[0])-96, int(c[1])
    return sum([1<=(x+i)<=8 and 1<=(y+j)<=8 for i in [-2,-1,1,2] for j in [-2,-1,1,2]])//2
    
    
    java solution
    int moves = 8;
    if (cell.charAt(0) == 'b' || cell.charAt(0) == 'g') {
        moves -= 2;
    }
    if (cell.charAt(1) == '2' || cell.charAt(1) == '7') {
        moves -= 2;
    }
    if (cell.charAt(0) == 'a' || cell.charAt(0) == 'h') {
        moves /= 2;
    }
    if (cell.charAt(1) == '1' || cell.charAt(1) == '8') {
        moves /= 2;
    }
    return moves;
'''
