def solution(array):
    count = 0

    for i in set(array):
        if count<array.count(i):
            count = array.count(i)
            answer = i
        elif count==array.count(i):
            count = array.count(i)
            answer = -1
    
    return answer