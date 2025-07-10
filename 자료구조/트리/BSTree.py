class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)
    
def search_bst_iter(n,key):
    if n == None:
        return None
    while n.key != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.rigth is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False
    
def delete_bst_case1(parent, node, root): # 단말 노드 삭제
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    return root

def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right
    
    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    
    return root

def delete_bst_case3(parent, node, root):
    succp = node                    # 후계자의 부모노드
    succ = node.right               # 후계자 노드
    while (succ.left != None):      # 후계자와 부모노드 탐색
        succp = succ
        succ = succ.left

    if (succp.left == succ):        # 후계자의 왼쪽 자식이면
        succp.left = succ.right     # 후계자의 오른쪽 자식 연결
    else:                           # 후계자의 오른쪽 자식이면
        succp.right = succ.right    # 후계자의 왼쪽 자식 연결
    
    node.key = succ.key
    node.value = succ.value
    node = succ

    return root

def delete_bst(root, key):
    if root == None : return None

    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key : node = node.left
        else: node = node.right

    if node == None: return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)
    
    return root

