# 파랑: 2가지
# 노랑: 1가지
# 주황: 8가지
# 초록: 4가지
# 보라: 4가지
# 총: 19가지
# 시간 복잡도: 19 * 4 * 500 * 500 => 2000만 정도?
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def blue(x, y):
    global answer
    # 가로
    b1 = 0
    if y+3 <= m-1:
        for i in range(y,y+4):
            b1 += paper[x][i]
    
    b2 = 0
    if x+3 <= n-1:
        for i in range(x,x+4):
            b2 += paper[i][y]
        
    
    answer = max(answer, max(b1,b2))

def yellow(x,y):
    global answer
    y1 = 0
    if x+2 < n and y+2 < m:
        for i in range(x,x+2):
            for j in range(y,y+2):
                y1 += paper[i][j]
    
    answer = max(y1, answer)

def orange(x,y):
    global answer
    # 세로
    o1 = []
    if x+2 < n and y+1 < m:
        o1.append(paper[x][y] + paper[x+1][y] + paper[x+2][y] + paper[x+2][y+1])
        o1.append(paper[x][y] + paper[x][y+1] + paper[x+1][y] + paper[x+2][y])
        o1.append(paper[x][y] + paper[x][y+1] + paper[x+1][y+1] + paper[x+2][y+1])
        o1.append(paper[x][y+1] + paper[x+1][y+1] + paper[x+2][y+1] + paper[x+2][y])
    
    if x+1 < n and y+2 < m:
        o1.append(paper[x][y] + paper[x][y+1] + paper[x][y+2] + paper[x+1][y+2])
        o1.append(paper[x][y] + paper[x+1][y] + paper[x][y+1] + paper[x][y+2])
        o1.append(paper[x+1][y] + paper[x+1][y+1] + paper[x+1][y+2] + paper[x][y+2])
        o1.append(paper[x][y] + paper[x+1][y] + paper[x+1][y+1] + paper[x+1][y+2])
    
    if o1:
        answer = max(answer, max(o1))

def green(x,y):
    global answer
    g1 = []
    if x+2 < n and y+1 < m:
        g1.append(paper[x][y] + paper[x+1][y] + paper[x+1][y+1] + paper[x+2][y+1])
        g1.append(paper[x][y+1] + paper[x+1][y] + paper[x+1][y+1] + paper[x+2][y])
    
    if x+1 < n and y+2 < m:
        g1.append(paper[x][y+1] + paper[x][y+2] + paper[x+1][y] + paper[x+1][y+1])
        g1.append(paper[x][y] + paper[x][y+1] + paper[x+1][y+1] + paper[x+1][y+2])
    
    if g1:
        answer = max(answer, max(g1))

def pupple(x,y):
    global answer
    p1 = []
    if x+1 < n and y+2 < m:
        p1.append(paper[x+1][y] + paper[x+1][y+1] + paper[x][y+1] + paper[x+1][y+2])
        p1.append(paper[x][y] + paper[x][y+1] + paper[x+1][y+1] + paper[x][y+2])

    if x+2 < n and y+1 < m:
        p1.append(paper[x][y] + paper[x+1][y] + paper[x+1][y+1] + paper[x+2][y])
        p1.append(paper[x][y+1] + paper[x+1][y] + paper[x+1][y+1] + paper[x+2][y+1])
    
    if p1:
        answer = max(answer, max(p1))

for i in range(n):
    for j in range(m):
        blue(i,j)
        yellow(i,j)
        orange(i,j)
        green(i,j)
        pupple(i,j)

print(answer)