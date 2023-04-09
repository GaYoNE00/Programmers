def solution(spell, dic):
    a = 2
    spell.sort()
    for i in range(len(dic)):
        dic[i] = sorted(dic[i])
        if dic[i] == spell:
            a = 1
    return a