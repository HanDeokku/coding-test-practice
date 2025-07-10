n = int(input())

first_building = int(input())

stack = []
stack.append(first_building)

answer = 0

for _ in range(n-1):
    new_building = int(input())
    
    while(stack):
        if new_building < stack[-1]:
            stack.append(new_building)
            break
        else:
            stack.pop()
        
    if not stack:
        stack.append(new_building)

    answer += len(stack) - 1

print(answer)