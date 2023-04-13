def solution(score):
    a = []
    b = []
    ranker = []
    for j in score:
            print(j)
            a.append(sum(j))
    b = list(a)
    b.sort(reverse=True)
    for i in a:
        ranker.append(b.index(i)+1)
    return ranker