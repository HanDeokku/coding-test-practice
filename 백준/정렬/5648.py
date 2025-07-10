import sys
input = sys.stdin.readline

first_input = input().split()

n = int(first_input[0])

arr = []

if len(first_input) > 1:
    for i in range(1,len(first_input)):
        arr.append(int(first_input[i][::-1]))

while len(arr) != n:
    nums = input().split()
    for i in range(len(nums)):
        arr.append(int(nums[i][::-1]))

arr.sort()

for num in arr:
    print(num)