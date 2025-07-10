n, m = map(int, input().split())

arr = [0] * m
visited = [False] * (n+1)

def back(x):
    global arr, visited
    if x == m:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            arr[x] = i
            visited[i] = True
            back(x+1)
            visited[i] = False

back(0)