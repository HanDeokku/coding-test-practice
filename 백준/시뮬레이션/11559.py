from collections import deque

puyo = [list(input().strip()) for _ in range(12)]

dx = [0,1,-1,0]
dy = [-1,0,0,1]

answer = 0

while True:
    visit = [[False] * 6 for _ in range(12)]
    check = False
    for i in range(11,-1,-1):
        for j in range(6):
            if puyo[i][j] != '.' and not visit[i][j]:
                cnt = 0
                queue = deque([(i,j)])
                visit[i][j] = True
                change_list = [(i,j)]
                while queue:
                    x, y = queue.popleft()
                    cnt += 1

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx > 11 or nx < 0 or ny > 5 or ny < 0: continue
                        if not visit[nx][ny] and puyo[i][j] == puyo[nx][ny]:
                            queue.append((nx,ny))
                            visit[nx][ny] = True
                            change_list.append((nx,ny))

                
                if cnt >= 4:
                    for a, b in change_list:
                        puyo[a][b] = '.'
                    check = True
    
    

    for i in range(11,-1,-1):
        for j in range(6):
            index = -1
            if puyo[i][j] != '.' :
                for k in range(i,12):
                    if puyo[k][j] == '.':
                        index = k

                if index == -1: continue
                puyo[index][j] = puyo[i][j]
                puyo[i][j] = '.'

    if check:
        answer += 1
        continue
    else:
        break

print(answer)