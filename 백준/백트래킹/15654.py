n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

answer = [0] * m

visited = [False] * n

def back(x):
    global answer, visited
    if x == m:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(n):
        if not visited[i]:
            answer[x] = arr[i]
            visited[i] = True
            back(x+1)
            visited[i] = False

back(0)