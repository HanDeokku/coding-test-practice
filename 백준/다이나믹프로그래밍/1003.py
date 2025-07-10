# f(1) = 0,1, f(2) = 1,1 f(3) = 1,2 f(4) = 2,3

t = int(input())
for _ in range(t):
    n = int(input())
    a, b = 1, 0
    for i in range(1,n+1):
        a, b = b, a+b
    print(a,b)