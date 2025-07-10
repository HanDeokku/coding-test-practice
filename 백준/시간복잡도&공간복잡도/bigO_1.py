def func1(n):
    hap = 0
    for num in range(1,n):
        if num % 3 == 0 or num % 5 == 0:
            hap += num

    return hap

n = int(input())

print(func1(n)) 