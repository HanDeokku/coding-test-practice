n = int(input())

visited1 = [False] * n
visited2 = [False] * (2*n-1)
visited3 = [False] * (2*n-1)

answer = 0

def back(x):
    global visited1, visited2, visited3, answer
    if x == n:
        answer += 1
        return
    
    for y in range(n):
        if visited1[y] or visited2[x+y] or visited3[x-y+n-1]: continue
        visited1[y] = True
        visited2[x+y] = True
        visited3[x-y+n-1] = True
        back(x+1)
        visited1[y] = False
        visited2[x+y] = False
        visited3[x-y+n-1] = False

back(0)

print(answer)