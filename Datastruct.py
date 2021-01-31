#Linked list singly

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

    
def printlist(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third
printlist(head)

