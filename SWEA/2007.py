t = int(input())

for case in range(1, t+1):
    s = input()
    answer = ''
    for p in range(1, 11):
        first = s[0:p]
        check = True
        for i in range(p, 30 - (30%p), p):
            if first != s[i:i+p]:
                check = False
                break

        if not check:
            continue
        else:
            answer = p
            break
    print(f'#{case} {answer}')

            