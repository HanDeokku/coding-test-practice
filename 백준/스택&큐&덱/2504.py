bracket = input()

stack = []
tmp = 1
answer = 0

for i in range(len(bracket)):
    now = bracket[i]
    if now == '(':
        stack.append(now)
        tmp *= 2
    elif now == '[':
        stack.append(now)
        tmp *= 3
    elif now == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if bracket[i-1] == '(':
            answer += tmp
        
        stack.pop()
        tmp = tmp // 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if bracket[i-1] == '[':
            answer += tmp
        
        stack.pop()
        tmp = tmp // 3

if stack:
    print(0)
else:
    print(answer)