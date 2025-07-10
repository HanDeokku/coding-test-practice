stick = input()

stack = []
stack.append(stick[0])
cnt = 0

for i in range(1,len(stick)):
    last = stick[i-1]
    now = stick[i]
    if now == '(':
        stack.append(now)
    else:
        stack.pop()
        if last == now:
            cnt += 1
        else:
            cnt += len(stack)

print(cnt)