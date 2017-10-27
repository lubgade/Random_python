# Find the middle node of a linked list using 2 pointers
# Linear time O(n)

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


n1 = Node("Hello", None)
n2 = Node("21", n1)
n3 = Node("Green", n2)
n4 = Node("Blue", n3)
n5 = Node("Daniel", n4)


head = n5

fastptr = head
slowptr = head

while fastptr.next != None and fastptr.next.next != None:
    fastptr = fastptr.next.next
    slowptr = slowptr.next

print slowptr.data