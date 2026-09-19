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

def find_path(root, target, path):
    if root is None:
        return False
    path.append(root)
    if root.val == target:
        return True
    if find_path(root.left, target, path) or find_path(root.right, target, path):
        return True
    path.pop()
    return False

print("Build the tree:")
root = build_tree()

p_val = int(input("Enter value of p: "))
q_val = int(input("Enter value of q: "))

path_p = []
path_q = []

find_path(root, p_val, path_p)
find_path(root, q_val, path_q)

i = 0
while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
    i = i + 1

lca = path_p[i - 1]
print("Lowest Common Ancestor:", lca.val)