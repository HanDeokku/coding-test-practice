n, s = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

def back(x,summ):
    global answer
    if x == n:
        if summ == s:
            answer += 1
        return
    
    back(x+1, summ)
    back(x+1, summ+arr[x])
            

summ = 0
back(0,summ)

if s == 0: print(answer-1)
else:
    print(answer)