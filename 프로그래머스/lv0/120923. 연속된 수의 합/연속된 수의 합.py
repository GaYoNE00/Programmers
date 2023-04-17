def solution(num, total):
    answer = [i for i in range(num)]
    mid = total//num
    if num%2 ==0:
        l = num//2-1
    else:
        l = num//2
    print(l)
    for i in range(l,num):
        answer[i] = mid
        mid +=1

        
    mid = total//num
    for i in range(l,-1,-1):
        answer[i] = mid
        mid -=1

    return answer