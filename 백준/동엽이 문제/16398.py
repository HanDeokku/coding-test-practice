import sys

n = int(input())

matrix = []

for i in range(n):
    row = list(map(int,sys.stdin.readline().split()))
    matrix.append(row)

visited = [0]
answer = 0

while len(visited) < n:
    cost = 10000000000
    next = -1
    for node in visited:
        for i in range(n):
            if i not in visited:
                if cost > matrix[node][i]:
                    cost = matrix[node][i]
                    next = i
    visited.append(next)
    answer += cost
    
print(answer)