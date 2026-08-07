class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_start(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None

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

start = find_start(head)

if start:
    print("Start:", start.value)
else:
    print("No cycle")