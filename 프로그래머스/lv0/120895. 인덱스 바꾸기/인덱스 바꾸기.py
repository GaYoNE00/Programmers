def solution(my_string, num1, num2):
    j = 0
    answer = ""
    for i in my_string:
        if j == num1:
            answer += my_string[num2]
        elif j == num2:
            answer += my_string[num1]
        else:
            answer += i            
        j += 1
    return answer