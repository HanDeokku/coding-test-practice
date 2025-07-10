n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
ans = [0] * m

def back(x,index):
    if x == m:
        print(" ".join(map(str, ans)))
        return

    for i in range(index,n):
        ans[x] = arr[i]
        back(x+1,i)
    
back(0,0)