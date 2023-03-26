def solution(n):
    answer = []
    rm = []
    for i in range(2,n+1):
        if n%i == 0:
            answer.append(i)
            n = n//i
    for j in answer:
        for k in range(2,j):
            if j == 2:
                continue
            if j%k==0:
                print(j)
                rm.append(j)
                break
    for i in rm:
        answer.remove(i)
    return sorted(answer)