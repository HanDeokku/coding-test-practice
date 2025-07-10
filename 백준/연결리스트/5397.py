n = int(input())

for _ in range(n):
    keyinput = input()
    l_stack = []
    r_stack = []
    for key in keyinput:
        if key == '-':
            if l_stack:
                l_stack.pop()
        elif key == '<':
            if l_stack:
                r_stack.append(l_stack.pop())
        elif key == '>':
            if r_stack:
                l_stack.append(r_stack.pop())
        else:
            l_stack.append(key)
    
    if r_stack:
        l_stack.extend(reversed(r_stack))
    
    print(''.join(l_stack))