def solution(a, b, n):

    ans = 0
    for i in range(n):
        ans += a*b
        a += 1
        b += 1
    return ans
