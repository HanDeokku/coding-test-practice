n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

now = 1
last = 1
answer = arr[0]
for i in range(n-1):
    if arr[i] != arr[i+1]:
        if last < now:
            answer = arr[i]
            last = now
        now = 1
    else:
        now += 1
    
    if i == n-2:
        if last < now:
            answer = arr[i]


print(answer)