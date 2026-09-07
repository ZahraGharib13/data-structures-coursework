n = int(input())
tree = []
qs = []
is_child = [False]*(n+1)
is_child[0] = True
search_dic = {}

for i in range(n-1):
    p, c, d = input().split()
    p = int(p)
    c = int(c)
    qs.append((p, c, d))

    if p not in search_dic:
        search_dic[p] = {}
    search_dic[p][d] = c

    is_child[int(c)] = True

def find_root():
    return is_child.index(False)

class Node:
    def __init__(self, root):
        self.root = root 

    def element(self):
        return self.root

    def left(self):
        if self.root in search_dic and 'left' in search_dic[self.root]:
            return Node(search_dic[self.root]['left'])
        return None

    def right(self):
        if self.root in search_dic and 'right' in search_dic[self.root]:
            return Node(search_dic[self.root]['right'])
        return None

def inorder(root):
    if not root:
        return
    inorder(root.left())
    tree.append(str(root.element()))
    inorder(root.right())

inorder(Node(find_root()))

print(" ".join(tree))
                