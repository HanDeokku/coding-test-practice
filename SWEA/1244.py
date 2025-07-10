t = int(input())
for case in range(1, t+1):
    num, n = map(int, input().split())
    nums = list(str(num))
    while n:
        for i in range(len(nums)):
            max_num = nums[i]
            index = i
            for j in range(i+1, len(nums)):
                if max_num <= nums[j]:
                    max_num = nums[j]
                    index = j
            if index != i:
                temp = nums[i]
                nums[i] = nums[index]
                nums[index] = temp
                n -= 1
            if n == 0:
                break
        
        if n != 0:
            if n % 2 == 1:
                tmp = nums[-1]
                nums[-1] = nums[-2]
                nums[-2] = tmp
                break
            else:
                break

    answer = ''.join(nums)
    print(f'#{case} {answer}')