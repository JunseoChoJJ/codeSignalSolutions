def solution(bishop, pawn):
    # a -> c count 1 -> 3 count should be the same
    
    count = abs(ord(bishop[0]) - ord(pawn[0]))
    count2 = abs(int(bishop[1]) - int(pawn[1]))
    
    if count == count2:
        return True
    else:
        return False
