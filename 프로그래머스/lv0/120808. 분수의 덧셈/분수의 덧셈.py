def solution(numer1, denom1, numer2, denom2):
    t = (numer1*denom2) + (numer2*denom1)
    b = denom1*denom2
    m = 1
    for i in range(1,t+1):
        if (t%i==0) and (b%i==0):
            m = i
    answer = [t//m,b//m]
    return answer