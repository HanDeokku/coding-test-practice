import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

q1 = deque(arr1)
q2 = deque(arr2)

answer = []

while True:
    if not q1:
        answer.extend(q2)
        break

    if not q2:
        answer.extend(q1)
        break

    num1 = q1.popleft()
    num2 = q2.popleft()

    if num1 > num2:
        answer.append(num2)
        q1.appendleft(num1)
    else:
        answer.append(num1)
        q2.appendleft(num2)

for a in answer:
    print(a, end=' ')