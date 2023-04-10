def solution(n):
    answer = 1
    for i in range(2,n+1,1):
        answer += 1
        while True:
            if answer%3 == 0 or str(answer).count("3") > 0:
                answer += 1
            else:
                break
    return answer