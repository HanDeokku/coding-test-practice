import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    d = [0,1,1,1,2,2]
    for i in range(6,n+1):
        d.append(d[i-5] + d[i-1])
    
    print(d[n])