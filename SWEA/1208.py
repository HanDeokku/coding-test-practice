import heapq

for case in range(1, 2):
    dump1 = int(input())
    dump2 = dump1
    nums = list(map(int, input().split()))
    heapq.heapify(nums)
    while dump1:
        tmp = heapq.heappop(nums)
        heapq.heappush(nums, tmp + 1)
        dump1 -= 1
    
    heap = []
    for num in nums:
        heapq.heappush(heap, (-num, num))

    while dump2:
        _, tmp = heapq.heappop(heap)
        temp = tmp - 1
        heapq.heappush(heap, (-temp, temp))
        dump2 -= 1
    
    _, mx = heapq.heappop(heap)
    mn = heapq.heappop(nums)
    answer = mx - mn
    print(f'#{case} {answer}')