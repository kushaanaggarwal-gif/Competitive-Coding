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

total_nodes = int(input("How many nodes in the BST? "))

root = None
for i in range(total_nodes):
    v = int(input("Enter node value: "))
    root = insert_bst(root, v)

p_val = int(input("Enter target value p: "))

successor = None
curr = root

while curr is not None:
    if p_val >= curr.val:
        curr = curr.right
    else:
        successor = curr
        curr = curr.left

if successor is not None:
    print("Inorder Successor:", successor.val)
else:
    print("Inorder Successor: None")