import sys, heapq

n = int(input())

matrix = []

for i in range(n):
    row = list(map(int,sys.stdin.readline().split()))
    matrix.append(row)

visited = [False] * n
heap = [(0,0)]
answer = 0
cnt = 0

while cnt < n:
    cost, node = heapq.heappop(heap)
    
    if visited[node]:
        continue

    answer += cost
    visited[node] = True

    cnt += 1

    for next in range(n):
        if not visited[next]:
            heapq.heappush(heap, (matrix[node][next], next))

    
print(answer)