class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def detect_cycle(head):
    seen = set()

    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next

    return False

n = int(input("n: "))
arr = list(map(int, input("Values: ").split()))

head = Node(arr[0])
temp = head

for i in range(1, n):
    temp.next = Node(arr[i])
    temp = temp.next

if detect_cycle(head):
    print("Cycle detected")
else:
    print("No cycle")