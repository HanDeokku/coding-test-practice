from collections import deque

students = [list(input()) for _ in range(5)]
visited = [False] * 25

arr = []
comb = []

def bfs(s):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    l = [i for i in s]
    q = deque([l[0]])
    l.remove(l[0])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx > 4 or nx < 0 or ny > 4 or ny < 0: continue
            if (nx,ny) in l:
                q.append((nx,ny))
                l.remove((nx,ny))
        if not l:
            return True
    
    return False




for i in range(5):
    for j in range(5):
        arr.append((i,j))

sub = [(0,0)] * 7
n = []
s = []
answer = 0

def back(x,index):
    global answer
    if x == 7:
        if n.count('S') >= 4 and bfs(s):
            answer += 1
        return

    for i in range(index,25):
        a,b = arr[i]
        s.append((a,b))
        n.append(students[a][b])
        back(x+1,i+1)
        n.pop()
        s.pop()
        

back(0,0)

print(answer)