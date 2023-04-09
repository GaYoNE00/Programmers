def solution(sides):
    return (max(sides)-(sum(sides)))*-1+sum(sides)-(max(sides)+1)
