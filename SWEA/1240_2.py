t = int(input())

def function(arr):
    cnt = 1
    result = []
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            cnt += 1
        else:
            result.append(str(cnt))
            cnt = 1
    result.append(str(cnt))
    
    s = ''.join(result)
    
    if s == '3211':
        return 0
    elif s == '2221':
        return 1
    elif s == '2122':
        return 2
    elif s == '1411':
        return 3
    elif s == '1132':
        return 4
    elif s == '1231':
        return 5
    elif s == '1114':
        return 6
    elif s == '1312':
        return 7
    elif s == '1213':
        return 8
    else:
        return 9

for c in range(1, t + 1):
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]

    password = []
    check = False

    for i in range(n):
        if '1' in matrix[i]:
            idx = matrix[i].rfind('1')
            password = matrix[i][idx - 55:idx + 1]
            check = True
            break

    if not check or len(password) != 56:
        print(f'#{c} 0')
        continue
    
    p1 = function(password[0:7])
    p2 = function(password[7:14])
    p3 = function(password[14:21])
    p4 = function(password[21:28])
    p5 = function(password[28:35])
    p6 = function(password[35:42])
    p7 = function(password[42:49])
    p8 = function(password[49:56])

    num = (p1 + p3 + p5 + p7) * 3 + p2 + p4 + p6 + p8
    if num % 10 == 0:
        answer = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
        print(f'#{c} {answer}')
    else:
        print(f'#{c} 0')
