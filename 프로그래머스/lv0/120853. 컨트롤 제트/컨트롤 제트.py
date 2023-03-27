def solution(s):
    answer = 0
    a = []
    b = []
    c = []
    a = s.split()
    c = s.split()
    
    for i in range(len(a)):
        if a[i]=="Z":
            b.append(a[i-1])
            c.remove("Z")
            
    for i in c:
        if float(i).is_integer:
            answer += float(i)
    
    for i in b:
        if float(i).is_integer:
            answer -= float(i)
    
    return int(answer)