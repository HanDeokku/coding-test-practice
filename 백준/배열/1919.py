word1 = input()
word2 = input()

alpha1 = [0] * 26
alpha2 = [0] * 26

for word in word1:
    alpha1[ord(word)-97] += 1

for word in word2:
    alpha2[ord(word)-97] += 1

cnt = 0

for i in range(26):
    if alpha1[i] != alpha2[i]:
        cnt += abs(alpha1[i] - alpha2[i])

print(cnt)