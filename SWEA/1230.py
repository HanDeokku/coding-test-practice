for case in range(1, 11):
    n = int(input())
    passwords = list(map(int, input().split()))
    c = int(input())
    command = input().split()
    index = 0
    cnt = 1
    while cnt <= c:
        if command[index] == 'I':
            x = int(command[index + 1])
            y = int(command[index + 2])
            for i in range(index + 2 + y, index + 2, -1):
                num = int(command[i])
                passwords.insert(x ,num)
            index = index + 3 + y
        elif command[index] == 'D':
            x = int(command[index + 1])
            y = int(command[index + 2])
            del(passwords[x:x+y])
            index = index + 3
        else:
            y = int(command[index + 1])
            for i in range(index + 2, index + 2 + y):
                num = int(command[i])
                passwords.append(num)
            index = index + 2 + y
        cnt += 1
    print(f'#{case}', end=' ')
    for i in range(0,10):
        print(passwords[i], end=' ')