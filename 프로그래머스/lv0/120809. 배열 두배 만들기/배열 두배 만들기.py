def solution(numbers):
    b = []
    b = b+numbers
    answer = []
    for i in range(len(b)):
        answer.append(b.__getitem__(i)*2)

    return answer
