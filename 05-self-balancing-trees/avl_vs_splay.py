
n = int(input())
nodes = list(map(int, input().split()))

search_sequence = []
for _ in range(n):
    search_sequence.append(list(map(int, input().split())))

# -------------------
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def avl_height(node):
    return node.height if node else 0

def avl_update_height(node):
    if node:
        node.height = 1 + max(avl_height(node.left), avl_height(node.right))

def avl_balance_factor(node):
    return avl_height(node.left) - avl_height(node.right) if node else 0

def avl_rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    avl_update_height(y)
    avl_update_height(x)
    return x

def avl_rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    avl_update_height(x)
    avl_update_height(y)
    return y

def avl_insert(root, key):
    if not root:
        return AVLNode(key)
    
    if key < root.key:
        root.left = avl_insert(root.left, key)
    elif key > root.key:
        root.right = avl_insert(root.right, key)
    else:
        return root
    
    avl_update_height(root)
    balance = avl_balance_factor(root)
    
    if balance > 1 and key < root.left.key:
        return avl_rotate_right(root)
    if balance < -1 and key > root.right.key:
        return avl_rotate_left(root)
    if balance > 1 and key > root.left.key:
        root.left = avl_rotate_left(root.left)
        return avl_rotate_right(root)
    if balance < -1 and key < root.right.key:
        root.right = avl_rotate_right(root.right)
        return avl_rotate_left(root)
    
    return root

def avl_build(sequence):
    root = None
    for key in sequence:
        root = avl_insert(root, key)
    return root

def avl_search_depth(root, key):
    depth = 0
    curr = root
    while curr:
        if curr.key == key:
            return depth
        elif key < curr.key:
            curr = curr.left
        else:
            curr = curr.right
        depth += 1
    return 0

# ----------------
class SplayNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None
    
    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def _splay(self, node):
        while node.parent:
            parent = node.parent
            grandparent = parent.parent
            
            if not grandparent:
                #zig
                if node == parent.left:
                    self._right_rotate(parent)
                else:
                    self._left_rotate(parent)
            elif node == parent.left and parent == grandparent.left:
                # zigZig
                self._right_rotate(grandparent)
                self._right_rotate(parent)
            elif node == parent.right and parent == grandparent.right:
                # zag zag
                self._left_rotate(grandparent)
                self._left_rotate(parent)
            elif node == parent.right and parent == grandparent.left:
                # ZigZag
                self._left_rotate(parent)
                self._right_rotate(grandparent)
            else:
                # zag-zig
                self._right_rotate(parent)
                self._left_rotate(grandparent)
    
    def insert(self, key):
        node = SplayNode(key)
        if not self.root:
            self.root = node
            return
        
        current = self.root
        parent = None
        
        while current:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                self._splay(current)
                return
        
        node.parent = parent
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node
        
        self._splay(node)
    
    def _find_depth(self, key):

        depth = 0
        current = self.root
        while current:
            if current.key == key:
                return depth
            elif key < current.key:
                current = current.left
            else:
                current = current.right
            depth += 1
        return depth
    
    def search_cost(self, key):

        depth = self._find_depth(key)
        

        current = self.root
        while current:
            if current.key == key:
                break
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        
        if current:
            self._splay(current)
        
        return 2 * depth


avl_tree = avl_build(nodes)

results = []

for seq in search_sequence:
    avl_cost = 0
    for key in seq:
        avl_cost += avl_search_depth(avl_tree, key)
    
    splay_tree = SplayTree()
    for key in nodes:
        splay_tree.insert(key)
    
    splay_cost = 0
    for key in seq:
        splay_cost += splay_tree.search_cost(key)
    
    results.append((avl_cost, splay_cost))

for avl_cost, splay_cost in results:
    print(avl_cost, splay_cost)