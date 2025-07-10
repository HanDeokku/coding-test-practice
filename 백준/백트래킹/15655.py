n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

visited = [False]*n
answer = [0]*m

def back(x,index):
    global visited, answer
    if x == m:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(index, n):
        if not visited[i]:
            answer[x] = arr[i]
            visited[i] = True
            back(x+1,i)
            visited[i] = False
    
back(0,0)