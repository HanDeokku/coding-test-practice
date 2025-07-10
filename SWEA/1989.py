t = int(input())

for case in range(1, t+1):
    s = input()
    s_len = len(s)-1
    check = True
    for i in range(len(s)):
        if i >= s_len-i:
            break

        if s[i] != s[s_len-i]:
            check = False
    
    if check:
        print(f'#{case}', 1)
    else:
        print(f'#{case}', 0)