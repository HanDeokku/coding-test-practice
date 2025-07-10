t = int(input())

for case in range(1, t+1):
    n = int(input())
    pascal = [[1]]
    for i in range(1, n):
        add_pascal = []
        for j in range(i+1):
            if j == 0 or j == i:
                add_pascal.append(1)
            else:
                add_pascal.append(pascal[i-1][j-1] + pascal[i-1][j])
        
        pascal.append(add_pascal)
    
    print(f'#{case}')
    for i in range(n):
        for j in range(len(pascal[i])):
            print(pascal[i][j], end=' ')
        print()