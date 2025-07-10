import sys
input = sys.stdin.readline

n = int(input())

t = [0]
p = [0]

d = [0] * (n+1)

for _ in range(n):
    ti, pi = map(int,input().split())
    t.append(ti)
    p.append(pi)

for i in range(1, n+1):
    if i + (t[i]-1) < n+1:
        d[i+(t[i]-1)] = max(d[i-1]+p[i], d[i+(t[i]-1)])
        
    d[i] = max(d[i], d[i-1])

print(d[n])