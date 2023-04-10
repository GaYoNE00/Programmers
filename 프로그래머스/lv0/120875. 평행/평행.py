def solution(dots):
    dots = sorted(dots, key=lambda x: (x[0], x[1]))
    
    if dots[1][0] == dots[0][0] or dots[3][0] == dots[2][0]:
        return 0
    
    m1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    m2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    
    return 1 if m1 == m2 else 0
