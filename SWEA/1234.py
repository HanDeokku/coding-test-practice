for case in range(1, 11):
    n, password = input().split()
    passwords = list((password))
    index = 0
    while index < len(passwords):
        if index + 1 < len(passwords):
            if passwords[index] == passwords[index + 1]:
                del(passwords[index:index+2])
                if index != 0:
                    index -= 1
                continue
        index += 1
    answer = ''.join(passwords)
    print(f'#{case} {answer}')
        
## 9823