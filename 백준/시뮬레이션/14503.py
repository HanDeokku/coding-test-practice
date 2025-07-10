import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
r,c,d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

clean = [[False] * m for _ in range(n)]
q = deque()
q.append((r,c,d))

answer = 0

dx, dy = [1,0,-1,0], [0,1,0,-1]

while q:
    x, y, d = q.popleft()
    
    if not clean[x][y]: 
        clean[x][y] = True 
        answer += 1

    check = True

    for _ in range(4):
        if d == 0:
            if y-1 < 0 or y-1 > m-1:
                d = 3
                continue
            if room[x][y-1] == 0 and not clean[x][y-1]:
                q.append((x,y-1,3))
                check = False
                break
            else:
                d = 3
                continue
        elif d == 1:
            if x-1 < 0 or x-1 > n-1:
                d = 0
                continue
            if room[x-1][y] == 0 and not clean[x-1][y]:
                q.append((x-1,y,0))
                check = False
                break
            else:
                d = 0
                continue
        elif d == 2:
            if y+1 < 0 or y+1 > m-1:
                d = 1
                continue
            if room[x][y+1] == 0 and not clean[x][y+1]:
                q.append((x,y+1,1))
                check = False
                break
            else:
                d = 1
                continue
        else:
            if x+1 < 0 or x+1 > n-1:
                d = 2
                continue
            if room[x+1][y] == 0 and not clean[x+1][y]:
                q.append((x+1,y,2))
                check = False
                break
            else:
                d = 2
                continue
        
    if check:
        if d == 0:
            if x+1 < n and room[x+1][y] == 0:
                q.append((x+1,y,0))
            else:
                print(answer)
                exit()
        elif d == 1:
            if y-1 >= 0 and room[x][y-1] == 0:
                q.append((x,y-1,1))
            else:
                print(answer)
                exit()
        elif d == 2:
            if x-1 >= 0 and room[x-1][y] == 0:
                q.append((x-1,y,2))
            else:
                print(answer)
                exit()
        else:
            if y+1 < m and room[x][y+1] == 0:
                q.append((x,y+1,3))
            else:
                print(answer)
                exit()

print(answer)