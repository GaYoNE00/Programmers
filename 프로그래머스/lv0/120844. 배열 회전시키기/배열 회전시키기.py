def solution(numbers, direction):

    if direction == "right":
        numbers.insert(0,numbers[len(numbers)-1])
        numbers.pop(len(numbers)-1)
    else:
        numbers.append(numbers[0])
        numbers.pop(0)
        
    return numbers