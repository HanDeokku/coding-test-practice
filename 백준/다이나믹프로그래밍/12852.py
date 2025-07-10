import sys
input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)
pre = [0] * (n+1)

d[1] = 0
pre[1] = 0

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    pre[i] = i-1
    if i % 2 == 0 and d[i] > (d[i//2] + 1):
        d[i] = d[i//2] + 1
        pre[i] = i//2
    
    if i % 3 == 0 and d[i] > (d[i//3] + 1):
        d[i] = d[i//3] + 1
        pre[i] = i//3
    
print(d[n])
print(n, end=' ')
while n > 1:
    print(pre[n], end=' ')
    n = pre[n]