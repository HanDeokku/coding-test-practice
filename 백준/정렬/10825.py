import sys
input = sys.stdin.readline

n = int(input())

students = {}

for i in range(n):
    name, k, e, m = input().split()
    students[name] = [int(k),int(e),int(m),name]

sorted_students = sorted(students.items(), key=lambda x:(-x[1][0],x[1][1],-x[1][2],x[1][3]))

for i in range(n):
    print(sorted_students[i][0])