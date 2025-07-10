from collections import deque

t = int(input())

for _ in range(t):
    w,h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    sang = []
    fire = []
    s_v = [[False]*w for _ in range(h)]
    f_v = [[False]*w for _ in range(h)]
    
    s_q = deque()
    f_q = deque()

    for i in  range(h):
        add_s = []
        add_f = []
        for j in range(w):
            value = building[i][j]
            if value == '.':
                add_s.append(0)
                add_f.append(0)
            elif value == '#':
                add_s.append(-1)
                add_f.append(-1)
            elif value == '@':
                add_s.append(1)
                add_f.append(0)
                s_q.append((i,j))
                s_v[i][j] = True
            else:
                add_f.append(1)
                f_q.append((i,j))
                f_v[i][j] = True
                add_s.append(-1)
        sang.append(add_s)
        fire.append(add_f)

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while f_q:
        x, y = f_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > h-1 or nx < 0 or ny > w-1 or ny < 0: continue
            if f_v[nx][ny] or fire[nx][ny] == -1: continue
            fire[nx][ny] = fire[x][y] + 1
            f_q.append((nx,ny))
            f_v[nx][ny] = True
    
    while s_q:
        x, y = s_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > h-1 or nx < 0 or ny > w-1 or ny < 0: continue
            if s_v[nx][ny] or sang[nx][ny] == -1: continue
            if f_v[nx][ny]:    
                if sang[x][y] + 1 >= fire[nx][ny]: continue
            sang[nx][ny] = sang[x][y] + 1
            s_q.append((nx,ny))
            s_v[nx][ny] = True

    for i in range(h):
        for j in range(w):
            if not s_v[i][j]:
                sang[i][j] = -1
    
    answer = 10000001
    for i in range(0, w):
        if sang[0][i] == -1: continue
        if answer > sang[0][i]:
            answer = sang[0][i]

    for i in range(0, w):
        if sang[h-1][i] == -1: continue
        if answer > sang[h-1][i]:
            answer = sang[h-1][i]

    for i in range(0, h):
        if sang[i][0] == -1: continue
        if answer > sang[i][0]:
            answer = sang[i][0]

    for i in range(0, h):
        if sang[i][w-1] == -1: continue
        if answer > sang[i][w-1]:
            answer = sang[i][w-1]

    if answer == 10000001:
        print('IMPOSSIBLE')
    else:
        print(answer)