import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

directions = [0, 1, 2, 3]
answer = 0

def move(board, direction):
    new_board = [[0] * n for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    
    if direction == 0:  # 위로 이동
        for j in range(n):
            index = 0
            for i in range(n):
                if board[i][j] != 0:
                    if index > 0 and new_board[index-1][j] == board[i][j] and not visit[index-1][j]:
                        new_board[index-1][j] *= 2
                        visit[index-1][j] = True
                    else:
                        new_board[index][j] = board[i][j]
                        index += 1

    elif direction == 1:  # 왼쪽으로 이동
        for i in range(n):
            index = 0
            for j in range(n):
                if board[i][j] != 0:
                    if index > 0 and new_board[i][index-1] == board[i][j] and not visit[i][index-1]:
                        new_board[i][index-1] *= 2
                        visit[i][index-1] = True
                    else:
                        new_board[i][index] = board[i][j]
                        index += 1

    elif direction == 2:  # 아래로 이동
        for j in range(n):
            index = n - 1
            for i in range(n-1, -1, -1):
                if board[i][j] != 0:
                    if index < n - 1 and new_board[index+1][j] == board[i][j] and not visit[index+1][j]:
                        new_board[index+1][j] *= 2
                        visit[index+1][j] = True
                    else:
                        new_board[index][j] = board[i][j]
                        index -= 1

    else:  # 오른쪽으로 이동
        for i in range(n):
            index = n - 1
            for j in range(n-1, -1, -1):
                if board[i][j] != 0:
                    if index < n - 1 and new_board[i][index+1] == board[i][j] and not visit[i][index+1]:
                        new_board[i][index+1] *= 2
                        visit[i][index+1] = True
                    else:
                        new_board[i][index] = board[i][j]
                        index -= 1

    return new_board

def backtrack(depth, board):
    global answer
    if depth == 5:
        answer = max(answer, max(map(max, board)))
        return
    
    for direction in directions:
        new_board = move(copy.deepcopy(board), direction)
        backtrack(depth + 1, new_board)

backtrack(0, board)
print(answer)