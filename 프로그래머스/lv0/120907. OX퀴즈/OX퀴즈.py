def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        a,b,c,d,e = quiz[i].split(" ")
        if eval(a+b+c) == int(e):
            answer.append("O")
        else:
            answer.append("X")
    return answer
