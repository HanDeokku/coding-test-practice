n, c = map(int,input().split())
arr = list(map(int, input().split()))

# 딕셔너리 사용하기?
# value 값 정렬
# value 값이 같은 것끼리 리스트에 넣고 먼저 나온 순서대로 정렬

d = {}

for a in arr:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1

sorted_arr = sorted(d.items(), key=lambda x:x[1], reverse=True)
sorted_dict = dict(sorted_arr)

l = len(sorted_arr)
answer = []

for i in range(l):
    if i == l-1:
        tmp = [sorted_arr[i][0]]

        for k in range(n):
            for t in tmp:
                if arr[k] == t and t not in answer:
                    tmp2 = [t] * sorted_dict[t]
                    answer.extend(tmp2)
        
        break


    tmp = [sorted_arr[i][0]]
    for j in range(i+1,l):
        if sorted_arr[i][1] == sorted_arr[j][1]:
            tmp.append(sorted_arr[j][0])
        else:
            break
    
    for k in range(n):
        for t in tmp:
            if arr[k] == t and t not in answer:
                tmp2 = [t] * sorted_dict[t]
                answer.extend(tmp2)

    i = j-1

for ans in answer:
    print(ans, end=' ')