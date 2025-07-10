l, c = map(int, input().split())

alpha = list(input().split())
alpha.sort()

password = [''] * l

vowel = ['a','e','i','o','u']

visit = [False] * c

def back(x, cnt1, cnt2, next):
    if x == l:
        print(''.join(map(str, password)))
        return

    for i in range(next, c):
        if not visit[i]:
            if alpha[i] in vowel:
                if l - cnt1 <= 2: continue
                password[x] = alpha[i]
                visit[i] = True
                back(x+1, cnt1+1, cnt2, i)
                visit[i] = False
            else:
                if l - cnt2 <= 1: continue
                password[x] = alpha[i]
                visit[i] = True
                back(x+1, cnt1, cnt2+1, i)
                visit[i] = False

back(0, 0, 0, 0)

