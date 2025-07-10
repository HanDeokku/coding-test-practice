n, m = map(int, input().split())

arr = list(map(int, input().split()))
visited = [False] * n
arr.sort()
ans = [0] * m
ansSet = set()

def back(x,index):
    if x == m:
        ansSet.add(" ".join(map(str, ans)))
        return

    for i in range(index,n):
        if not visited[i]:
            ans[x] = arr[i]
            visited[i] = True
            back(x+1, i)
            visited[i] = False
    
back(0,0)
answer = []
ansList = list(ansSet)
for a in ansList:
    sub = list(map(int, a.split()))
    answer.append(sub)

answer.sort()

for a in answer:
    print(" ".join(map(str, a)))