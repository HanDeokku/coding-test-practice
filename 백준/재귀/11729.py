k = int(input())

answer = []
cnt = 0

def move(a, b, c, n):
    global cnt
    if n == 1:
        answer.append((a,c))
        return
    move(a, c, b, n-1)
    answer.append((a,c))
    move(b, a, c, n-1)

move(1, 2, 3, k)

print(answer)