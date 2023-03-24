def solution(n):
    i = 1
    rs = 1
    while n>=rs:
        i+=1
        rs = rs * i
    return i-1