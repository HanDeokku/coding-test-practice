n = int(input())

answer = 0
for _ in range(n):
    words = input()
    stack = []

    stack.append(words[0])
    for word in words[1:]:
        if stack:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        else:
            stack.append(word)
    
    if not stack:
        answer += 1

print(answer)