def func4(n):
    import math
    for i in range(0, 28):
        a = math.pow(2, i)
        if n < a:
            return int(math.pow(2, i-1))
    
    return 0

print(func4(int(input())))