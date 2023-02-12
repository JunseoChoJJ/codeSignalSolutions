def solution(yourLeft, yourRight, friendsLeft, friendsRight):

    me = sorted([yourLeft, yourRight])
    friend = sorted([friendsLeft, friendsRight])

    return me == friend
