import sys
input = sys.stdin.readline
t = int(input())

def gcd(a,b):
    if a == 0: return b
    return gcd(b%a, a)

for _ in range(t):
    m,n,x,y = map(int, input().split())

    c = x
    d = y

    if m == x: c = 0
    if n == y: d = 0

    a = min(m,n)
    b = max(m,n)
    lcm = int(a / gcd(a,b) * b)

    answer = -1

    for i in range(x,lcm+1,m):
        if i % n == d:
            answer = i
            break
    
    print(answer)