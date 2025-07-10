import sys
input = sys.stdin.readline

n = int(input())
flowers = []

for i in range(n):
    m1,d1,m2,d2 = map(int, input().split())
    flowers.append((m1,d1,m2,d2))

flowers.sort()

i = 0
answer = 0
last_date = (3,1)

while i < n:
    sm,sd,em,ed = flowers[i]

    if (sm, sd) <= last_date <= (em, ed):
        max_emd = (em,ed)
        while i < n-1:
            nsm,nsd,nem,ned = flowers[i+1]
            if last_date < (nsm, nsd):
                break
            if max_emd < (nem, ned):
                max_emd = (nem, ned)
            i += 1
        
        answer += 1
        last_date = max_emd

        if last_date > (11, 30):
            print(answer)
            exit(0)
    
    i += 1

print(0)