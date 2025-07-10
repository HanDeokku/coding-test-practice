from collections import deque

n, k = map(int, input().split())
dq = deque()

for i in range(1, n+1):
    dq.append(i)

answer = []

cnt = 0
while(dq):
    cnt += 1
    if cnt == k:
        answer.append(dq.popleft())
        cnt = 0
    else:
        dq.append(dq.popleft())
    

print("<", end='')
for num in answer[:-1]:
    print(num, end=', ')
print(f"{answer[-1]}>")