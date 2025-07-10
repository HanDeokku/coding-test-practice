import sys, itertools
input=sys.stdin.readline 

t = int(input()) 

for i in range(t):
    n = int(input())
    vectors = []
    x_sum = 0
    y_sum = 0
    for j in range(n):
        x, y = map(int, input().split())
        vectors.append((x,y))
        x_sum += x
        y_sum += y
    
    vectorsList = list(itertools.combinations(vectors, len(vectors)//2))

    answer = []
    
    for vecList in vectorsList[:len(vectorsList)//2]:
        x1 = 0  
        y1 = 0
        for a, b in vecList:
            x1 += a
            y1 += b
        
        ans_x = x_sum - x1
        ans_y = y_sum - y1
        answer.append(((ans_x-x1)**2 + (ans_y-y1)**2)**(0.5))
    
    print(min(answer))



    
