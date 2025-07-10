import sys
input = sys.stdin.readline
n, l = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

def line_check(line):
    slope = [False] * n
    for i in range(1, n):
        if abs(line[i-1] - line[i]) > 1:
            return False
        else:
            if line[i-1] - line[i] == 1:
                for j in range(l):
                    if i+j >= n:
                        return False
                    if line[i] != line[i+j]:
                        return False
                    if slope[i+j]:
                        return False
                    if not slope[i+j]:
                        slope[i+j] = True
            
            elif line[i-1] - line[i] == -1:
                for j in range(l):
                    if i-1-j < 0:
                        return False
                    if line[i-1] != line[i-1-j]:
                        return False
                    if slope[i-1-j]:
                        return False
                    if not slope[i-1-j]:
                        slope[i-1-j] = True
    
    return True

answer = 0
for i in range(n):
    if line_check(board[i]):
        answer += 1
for j in range(n):
    if line_check([board[i][j] for i in range(n)]):
        answer += 1

print(answer)
