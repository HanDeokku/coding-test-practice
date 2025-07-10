from collections import deque

# dist[i] = i 노드의 거리
# move[j] = j 노드의 부모

n, k = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001

# 길을 다 출력 하는 함수
def route(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

    

# bfs
def bfs():
    q = deque([n])

    while q:
        x = q.popleft()

        if x == k:
            print(dist[x])
            route(x)
            return x

        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0: 
                dist[i] = dist[x] + 1
                move[i] = x
                q.append(i)

bfs()