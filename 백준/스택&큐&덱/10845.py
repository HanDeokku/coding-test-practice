from collections import deque
import sys

n = int(sys.stdin.readline())

q = deque()

for _ in range(n):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        if q:
            a = q.popleft()
            print(a)
            q.appendleft(a)
        else:
            print(-1)
    else:
        if q:
            a = q.pop()
            print(a)
            q.append(a)
        else:
            print(-1)