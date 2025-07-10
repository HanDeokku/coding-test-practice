def back(x,index):
    global ans, arr, visit
    if x == 6:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(index,len(arr)):
        if not visit[i]:
            ans[x] = arr[i]
            visit[i] = True
            back(x+1, i)
            visit[i] = False

sub = list(map(int, input().split()))
while(True):
    if not sub[0]:
        break
    m = sub[0]
    arr = sub[1:]
    ans = [0] * 6
    visit = [False] * len(arr)
    back(0,0)

    sub = list(map(int, input().split()))
    if not sub[0]:
        break
    print()