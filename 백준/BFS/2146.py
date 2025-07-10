from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

num = 1
world = [[[0] * 2 for _ in range(n)] for _ in range(n)]
world_q = deque()


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and world[i][j][0] == 0:
            queue = deque([(i, j)])
            world_q.append((i, j, -num))
            world[i][j][0] = -num
            world[i][j][1] = -num

            while queue:
                x, y = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and world[nx][ny][0] == 0:
                        world[nx][ny][0] = -num
                        world[nx][ny][1] = -num
                        queue.append((nx, ny))
                        world_q.append((nx, ny, -num))

            num += 1

visited = [[False] * n for _ in range(n)]
answer = []
while world_q:
    x, y, land = world_q.popleft()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if nx > n-1 or nx < 0 or ny > n-1 or ny < 0: continue
        # x,y가 대륙일 때
        if graph[x][y] == 1:
            # nx, ny가 바다일 때
            if graph[nx][ny] == 0:
                # 방문하지 않았을 때
                if not visited[nx][ny]:
                    world[nx][ny][0] = 1 # 대륙과 바로 이어지는건 1 
                    world[nx][ny][1] = land
                    visited[nx][ny] = True
                    world_q.append((nx, ny, land))
                # 방문 했을 때
                else:
                    # 다른 대륙끼리 만났을 때 다리 연결
                    if world[nx][ny][1] != land:
                         answer.append(world[nx][ny][0])
                    
        # x, y가 바다일 때
        else:
            # nx, ny가 바다일 때
            if graph[nx][ny] == 0:
                if not visited[nx][ny]:
                    world[nx][ny][0] = world[x][y][0] + 1
                    world[nx][ny][1] = land
                    visited[nx][ny] = True
                    world_q.append((nx, ny, land))
                else:
                    if world[nx][ny][1] != land:
                        answer.append(world[nx][ny][0] + world[x][y][0])

print(min(answer))