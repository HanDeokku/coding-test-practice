from collections import deque

students = [list(input()) for _ in range(5)]

arr = [(i,j) for i in range(5) for j in range(5)]

n = []
s = []
answer = 0

def bfs(s):
    l = [i for i in s]
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    q = deque([l[0]])
    l.remove(l[0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = dx[i] + x, dy[i] + y
            if nx > 4 or nx < 0 or ny > 4 or ny < 0: continue
            if (nx, ny) in l:
                q.append((nx,ny))
                l.remove((nx,ny))
        if not l:
            return True
    
    return False
    

def back(depth, index):
    global answer
    if depth == 7:
        if n.count('S') >= 4 and bfs(s):
            answer += 1
        return
    
    for i in range(index,25):
        x, y = arr[i]
        s.append((x,y))
        n.append(students[x][y])
        back(depth+1,i+1)
        s.pop()
        n.pop()


back(0,0)


print(answer)