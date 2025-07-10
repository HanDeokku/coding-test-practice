from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
dz = [1,-1]

while True:
    l, r, c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    building = []
    count = []
    visit = []
    for _ in range(l):
        layer = []
        count_layer = []
        visit_layer = []
        for _ in range(r):
            add = list(input())
            layer.append(add)

            count_add = [0] * c
            count_layer.append(count_add)

            visit_add = [False] * c
            visit_layer.append(visit_add)
        
        building.append(layer)
        count.append(count_layer)
        visit.append(visit_layer)
        input()

    t1, t2, t3 = 0, 0, 0

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    q = deque([(i,j,k)])
                    visit[i][j][k] == True

                    while q:
                        z,x,y = q.popleft()

                        for idx in range(4):
                            nx = dx[idx] + x
                            ny = dy[idx] + y

                            if nx > r-1 or nx < 0 or ny > c-1 or ny < 0: continue
                            if visit[z][nx][ny]: continue
                            if building[z][nx][ny] == '#': continue

                            count[z][nx][ny] = count[z][x][y] + 1
                            visit[z][nx][ny] = True
                            q.append((z,nx,ny))
                        
                        for idx in range(2):
                            nz = dz[idx] + z

                            if nz > l-1 or nz < 0: continue
                            if visit[nz][x][y]: continue
                            if building[nz][x][y] == '#': continue

                            count[nz][x][y] = count[z][x][y] + 1
                            visit[nz][x][y] = True
                            q.append((nz,x,y))

                if building[i][j][k] == 'E':
                    t1, t2, t3 = i, j, k

    if not visit[t1][t2][t3]:
        print("Trapped!")
    else:
        print(f"Escaped in {count[t1][t2][t3]} minute(s).")

                        