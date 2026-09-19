class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    val = int(input("Enter node value (-1 for no node): "))
    if val == -1:
        return None
    root = Node(val)
    print("Left child of", val)
    root.left = build_tree()
    print("Right child of", val)
    root.right = build_tree()
    return root

def find_lca(root, p, q):
    if root is None or root.val == p or root.val == q:
        return root

    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)

    if left is not None and right is not None:
        return root

    if left is not None:
        return left
    else:
        return right

print("Build the tree:")
root = build_tree()

p_val = int(input("Enter value of p: "))
q_val = int(input("Enter value of q: "))

ans = find_lca(root, p_val, q_val)
print("Lowest Common Ancestor:", ans.val)