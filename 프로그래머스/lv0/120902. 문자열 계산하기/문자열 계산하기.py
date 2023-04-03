def solution(my_string):
    tokens = my_string.split()  # 공백을 기준으로 문자열 분리
    nums = [int(tokens[i]) for i in range(0, len(tokens), 2)]  # 숫자만 추출
    ops = [tokens[i] for i in range(1, len(tokens), 2)]  # 연산자만 추출
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            result += nums[i+1]
        else:
            result -= nums[i+1]
    return result
