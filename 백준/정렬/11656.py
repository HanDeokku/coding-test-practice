word = input()
arr = []

w = len(word)

for i in range(w):
    arr.append(word[i:w])

arr.sort()

for a in arr:
    print(a)