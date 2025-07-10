n = int(input())

for _ in range(n):
    s1, s2 = input().split()
    s1 = sorted(s1)
    s2 = sorted(s2)

    check = True
    for a, b in zip(s1, s2):
        if a != b:
            print("Impossible")
            check = False
            break
    
    if check:
        print("Possible")