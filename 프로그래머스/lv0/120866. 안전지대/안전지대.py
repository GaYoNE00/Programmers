def solution(board):
    board_c = [row[:] for row in board]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for y in range(0,3):
                    for x in range(0,3):
                        if i-1+y>=len(board) or j-1+x>=len(board[i]) or i-1+y==-1 or j-1+x==-1:
                            continue
                        else:
                            board_c[i-1+y][j-1+x] = 1
    answer = sum(i.count(0) for i in board_c)  
    print(board_c) 
    return answer