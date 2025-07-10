n = int(input())

lis = list(map(int, input().split()))

answer = [-1] * n

stack = []

for i in range(n):
    while stack and lis[i] > lis[stack[-1]]:
        answer[stack[-1]] = lis[i]
        stack.pop()

    stack.append(i)

for i in range(n):
    print(answer[i], end=' ')