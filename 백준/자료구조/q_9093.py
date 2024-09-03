import sys

n = int(sys.stdin.readline())

for i in range(n):
    strings = sys.stdin.readline().split()
    new_strings = []
    for string in strings:
        new_str = ''
        for j in range(len(string)-1,-1,-1):
            new_str += string[j]
        new_strings.append(new_str)
    
    for s in new_strings:
        print(s, end=' ')
    print()