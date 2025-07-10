# 선택 정렬 : 리스트에서 가장 작은 숫자를 선택해서 앞쪽으로 옮기는 방법
# 첫번째 요소와 가장 작은 요소 자리 교환, 두번째 요소와 남은 가장 작은 요소 교환 .. 이런 방식으로 진행
# 시간복잡도 : O(n)

def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
    return A

A = [4,6,8,3,2,4,1,7]

B = selection_sort(A)

print(B)