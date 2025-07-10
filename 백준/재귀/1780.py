n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

count = [0]*3

def recursion(n, x, y, t):
    global count
    cnt = 0

    if n == 1:
        if paper[x][y] == t:
            return 1
        else:
            return 0
    
    cnt += recursion(n//3, x+0, y+n//3, t)
    cnt += recursion(n//3, x+0, y+n//3 * 2, t)
    cnt += recursion(n//3, x+0, y+0, t)
    cnt += recursion(n//3, x+n//3, y+n//3, t)
    cnt += recursion(n//3, x+n//3, y+n//3 * 2, t)
    cnt += recursion(n//3, x+n//3, y+0, t)
    cnt += recursion(n//3, x+n//3 * 2, y+n//3, t)
    cnt += recursion(n//3, x+n//3 * 2, y+n//3 * 2, t)
    cnt += recursion(n//3, x+n//3 * 2, y+0, t)

    if cnt == 9:
        return 1
    else:
        if t == -1:
            count[2] += cnt
        else:
            count[t] += cnt
        return 0
        
answer = [0] * 3

for i in range(2):
    answer[i] = recursion(n, 0, 0, i)
answer[2] = recursion(n, 0, 0, -1)


if count[2] == 0:
    print(answer[2])
else:
    print(count[2])
if count[2] == 0:
    print(answer[0])
else:
    print(count[0])
if count[1] == 0:
    print(answer[1])
else:
    print(count[1])