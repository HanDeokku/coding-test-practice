from collections import deque

f, s, g, u, d = map(int, input().split())

# f = 총 층 개수
# s = 강호가 지금 있는 층
# g = 가고가 하는 층

q = deque([s])
count = [0] * (f+1)
visit = [False] * (f+1)
visit[s] = True

while q:
    x = q.popleft()

    if x+u <= f and not visit[x+u]:
        count[x+u] = count[x] + 1
        visit[x+u] = True
        q.append(x+u)
    
    if x-d > 0 and not visit[x-d]:
        count[x-d] = count[x] + 1
        visit[x-d] = True
        q.append(x-d)

if not visit[g]:
    print("use the stairs")
else:
    print(count[g])
