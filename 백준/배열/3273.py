arr = [0] * 2000001

l = int(input())
nums = list(map(int, input().split()))
x = int(input())

answer = 0

for n in nums:
    if x > n:
        if arr[x-n] == 1:
            answer += 1
        
        arr[n] = 1

print(answer)