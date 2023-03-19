from copy import deepcopy

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
print(deepcopy(board))

def move (board, dir):
    if dir == 0: #동
        for i in range(n):
            top = n-1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if tmp == board[i][top]:
                        board[i][top] = tmp * 2
                        top -= 1
                    elif board[i][top] ==0:
                        board[i][top] = tmp
                    else:
                        top -= 1
                        board[i][top] = tmp
    elif dir == 1: #서
        for i in range(n):
            top = 0
            for j in range(1, n, 1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j]=0
                    if tmp==board[i][top]:
                        board[i][top] = tmp * 2
                        top += 1
                    elif board[i][top] == 0:
                        board[i][top] = tmp
                    else:
                        top += 1
                        board[i][top] = tmp
    elif dir == 2: #남
        for j in range(n):
            top= n-1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp
    else :  #북
        for j in range(n):
            top = 0
            for i in range(1, n, 1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp
    return board
    
def dfs(board, cnt):
    global result
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                result = max(result, board[i][j])
        return
    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt+1)

result = 0
dfs(board, 0)
print ( result )
