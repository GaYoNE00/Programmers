def solution(polynomial):
    x = [i for i in polynomial.split() if i[-1]=="x"]
    a = sum(int(i) for i in polynomial.split(" ") if i.isdigit())
    answer = ""
    xr = 0
    for i in x:
        if i == "x":
            xr += 1
        else:
            xr += int(i[0:-1])
    if a == 0:
        answer = str(xr)+"x"
    else:
        answer = str(xr)+"x + "+str(a)
    if xr == 1:
        answer = "x + "+str(a)
        if a == 0:
            answer = "x"
        else:
            answer = "x + "+str(a)
    elif xr == 0:
        answer = str(a)

    return answer