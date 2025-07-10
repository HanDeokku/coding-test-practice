from collections import deque

n, m = map(int, input().split())

glacier = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
for i in range(n):
    for j in range(m):
        if glacier[i][j] != 0:
            queue.append((i, j))

sub_queue = deque()
remain_glacier = deque()
years = 0
answer_check = False

#####################################
# 빙하 녹이기

while queue:
    x, y = queue.popleft()
    
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
        if glacier[nx][ny] == 0:
            cnt += 1
        
    if glacier [x][y] - cnt <= 0:
        glacier[x][y] = -1
        sub_queue.append((x, y))
    else:
        remain_glacier.append((x, y))

#####################################
# 빙하 녹은거 0으로 바꿔주고, queue에 남은 빙하 넣어주기

    if not queue:
        # 년수 추가
        years += 1

        while sub_queue:
            a, b = sub_queue.popleft()
            glacier[a][b] = 0
        queue.extend(remain_glacier)
        remain_glacier = deque()

        # 녹였는데 빙하가 없을 때
        if not queue:
            print("녹였는데 빙하가 없어")
            break
        
        # 빙하가 분리됐는지 확인
        visited = [[False] * m for _ in range(n)]
        visited[queue[0][0]][queue[0][1]] = True
        sub2_queue = deque()
        sub2_queue.append(queue[0])
        count = 1
        while sub2_queue:
            x, y = sub2_queue.popleft()
            print(x, y, glacier[x][y])
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx > n-1 or nx < 0 or ny > m-1 or ny < 0: continue
                if visited[nx][ny]: continue
                if glacier[nx][ny] != 0:
                    visited[nx][ny] = True
                    sub2_queue.append((nx, ny))
                    count += 1
    
        if len(queue) != count:
            print("빙하가 분리됨")
            print(len(queue), count)
            answer_check = True
            break

if answer_check:
    print(years)
else:
    print(0)