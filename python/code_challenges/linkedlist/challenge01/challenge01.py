# Write here the code challenge solution

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def printAll(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next

    def deleteNode(self, node):
        """
        to delete a node:
        """
        node.val = node.next.val
        node.next = node.next.next
       

if __name__ == "__main__":
    linkedList1 = LinkedList()
    node1 = Node("4")
    linkedList1.append(node1)

    node2 = Node("6")
    linkedList1.append(node2)

    node3 = Node("3")
    linkedList1.append(node3)

    node4 = Node("9")
    linkedList1.append(node4)

    linkedList1.deleteNode("3")
    linkedList1.printAll()

        