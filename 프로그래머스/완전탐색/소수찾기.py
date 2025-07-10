import itertools

def checkPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**(0.5))+1):
            if n % i == 0:
                return False
    return True

def solution(numbers):
    nums = list(numbers)
    answer = []
    temp = []
    for i in range(1, len(nums) + 1):
        temp += list(itertools.permutations(nums, i))
    
    prime = [int(''.join(n)) for n in temp]
    
    for n in prime:
        if checkPrime(n):
            answer.append(n)
    
    return len(set(answer))

# itertools

# premutations : 순열을 만들어주는 라이브러리
# conbinations : 조합을 만들어주는 라이브러리