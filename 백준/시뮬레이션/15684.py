import sys
input = sys.stdin.readline

def check_line():
    for i in range(n):
        start = i
        for j in range(h):
            if ladder[j][start] == 1:
                start += 1
            elif start > 0 and ladder[j][start-1] == 1:
                start -= 1
        if i != start:
            return False
    return True

def dfs(cnt,x,y):
    global answer
    if answer <= cnt:
        return
    if check_line():
        answer = min(cnt, answer)
        return
    if cnt == 3:
        return
    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0

        for j in range(now, n-1):
            if ladder[i][j] == 0:            
                ladder[i][j] = 1
                dfs(cnt+1, i, j+2)
                ladder[i][j] = 0

n, m, h = map(int, input().split())

ladder = [[0] * n for _ in range(h)]
for i in range(m):
    a,b = map(int,input().split())
    ladder[a-1][b-1] = 1

answer = 4
dfs(0,0,0)
if answer > 3:
    answer = -1
print(answer)