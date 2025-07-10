n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
ans = [0] * m
ansSet = set()

def back(x):
    if x == m:
        ansSet.add(" ".join(map(str, ans)))
        return

    for i in range(n):
        ans[x] = arr[i]
        back(x+1)
    
back(0)
answer = []
ansList = list(ansSet)
for a in ansList:
    sub = list(map(int, a.split()))
    answer.append(sub)

answer.sort()

for a in answer:
    print(" ".join(map(str, a)))