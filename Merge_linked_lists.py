class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def merge(L1, L2):
    L3 = Node(None, None)
    pL3 = L3
    while L1 != None and L2 != None:
        if L1.data <= L2.data:
            current = L1
            L1 = L1.next
            #print current.data

        else:
            current = L2
            L2 = L2.next
            #print current.data

        L3.next = current
        #print L3.data
        L3 = L3.next
        #print L3.data
    if L1 == None:
        L3.next = L2
    elif L2 == None:
        L3.next = L1


    return pL3



n3 = Node(10, None)
n2 = Node(3, n3)
n1 = Node(1, n2)
L1 = n1

n6 = Node(9, None)
n5 = Node(6, n6)
n4 = Node(5, n5)
L2 = n4

merged = merge(L1, L2)
while merged != None:
    print str(merged.data) + "->"
    merged = merged.next
print "None"
