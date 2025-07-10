def func3(n):
    import math
    d = math.pow(n, 0.5)
    if d * d == n:
        return 1
    else:
        return 0
    
print(func3(int(input())))