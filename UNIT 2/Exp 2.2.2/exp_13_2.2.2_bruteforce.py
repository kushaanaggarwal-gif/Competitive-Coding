class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def inorder(root, order):
    if root is None:
        return
    inorder(root.left, order)
    order.append(root)
    inorder(root.right, order)

total_nodes = int(input("How many nodes in the BST? "))

root = None
for i in range(total_nodes):
    v = int(input("Enter node value: "))
    root = insert_bst(root, v)

p_val = int(input("Enter target value p: "))

order = []
inorder(root, order)

ans = None
for i in range(len(order)):
    if order[i].val == p_val:
        if i + 1 < len(order):
            ans = order[i + 1]
        break

if ans is not None:
    print("Inorder Successor:", ans.val)
else:
    print("Inorder Successor: None")