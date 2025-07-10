n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

def sum_nums(words):
    sum_num = 0
    for a in words:
        if 48 <= ord(a) <= 57:
            sum_num += int(a)
    
    return sum_num


for i in range(n):
    for j in range(n-1-i):
        if len(words[j]) > len(words[j+1]):
            words[j], words[j+1] = words[j+1], words[j]
        elif len(words[j]) == len(words[j+1]):
            if sum_nums(words[j]) > sum_nums(words[j+1]):
                words[j], words[j+1] = words[j+1], words[j]
            elif sum_nums(words[j]) == sum_nums(words[j+1]):
                if words[j] > words[j+1]:
                    words[j], words[j+1] = words[j+1], words[j]

for i in range(n):
    print(words[i])