n = int(input())

stack = [(100000001, 0)]

tawers = list(map(int, input().split()))

for i in range(n):
    tawer = tawers[i]
    while (stack[-1][0] <= tawer):
        stack.pop()
    print(stack[-1][1], end=' ')
    stack.append((tawer, i+1))