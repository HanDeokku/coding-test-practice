a,b,c = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a % c
    
    x = solution(a, b//2, c)

    if b % 2 == 0:
        return x * x % c
    else:
        return x * x * a % c

print(solution(a,b,c))