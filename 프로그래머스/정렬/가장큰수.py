from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))

    answer = ''
    for s in numbers:
        answer += s
    
    return answer if answer[0] != '0' else '0'

## functools의 cmp_to_key : 원하는 기준으로 정렬하게 만들어준다