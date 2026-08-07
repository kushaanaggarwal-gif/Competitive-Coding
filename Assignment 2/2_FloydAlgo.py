class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def detect_cycle(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

n = int(input("n: "))
arr = list(map(int, input("Values: ").split()))

list1 = []

for num in arr:
    list1.append(Node(num))

for i in range(n - 1):
    list1[i].next = list1[i + 1]

pos = int(input("Pos: "))

if pos != -1:
    list1[-1].next = list1[pos]

head = list1[0]

if detect_cycle(head):
    print("Cycle detected")
else:
    print("No cycle")