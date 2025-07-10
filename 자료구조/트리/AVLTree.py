def rotateLL(A): # 루트 A의 왼쪽 자식 B의 왼쪽 서브트리에 노드가 추가 된 상황
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A): # 루트 A의 오른쪽 자식 B의 오른쪽 서브트리에 노드가 추가된 상황
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A): # 루트 A의 오른쪽 자식 B의 왼쪽 서브트리에 노드가 추가된 상황
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A): # 루트 A의 왼쪽 자식 B의 오른쪽 서브트리에 노드가 추가된 상황
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)