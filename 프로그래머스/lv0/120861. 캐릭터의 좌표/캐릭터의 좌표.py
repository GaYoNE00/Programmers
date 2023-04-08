def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput:
        if i == "left" and (board[0]-1)//-2<=answer[0]-1:
            answer[0] = answer[0] - 1
        if i == "right" and (board[0]-1)//2>=answer[0]+1:
            answer[0] = answer[0] + 1
        if i == "up" and (board[1]-1)//2>=answer[1]+1:
            answer[1] = answer[1] + 1
        if i == "down" and (board[1]-1)//-2<=answer[1]-1:
            answer[1] = answer[1] - 1
    return answer
