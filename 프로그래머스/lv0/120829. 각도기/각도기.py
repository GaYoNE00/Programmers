def solution(angle):
    if 0<angle and angle<90:
        answer = 1
    elif 90==angle:
        answer = 2
    elif 90<angle and angle<180:
        answer = 3
    elif 180==angle:
        answer = 4
        
    return answer