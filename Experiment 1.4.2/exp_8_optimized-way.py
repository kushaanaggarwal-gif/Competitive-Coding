class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(values):
    if not values:
        return None

    head = Node(values[0])
    temp = head

    for num in values[1:]:
        temp.next = Node(num)
        temp = temp.next

    return head

def is_palindrome(head):

    if head is None or head.next is None:
        return True

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    previous = None
    current = slow.next

    while current:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode

    first = head
    second = previous

    while second:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next

    return True

n = int(input("Enter number of nodes: "))

print("Enter the values of the linked list:")
values = []

for i in range(n):
    values.append(int(input()))

head = createLinkedList(values)

if is_palindrome(head):
    print("True")
else:
    print("False")