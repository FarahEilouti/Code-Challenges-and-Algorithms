# Write here the code challenge solution

from pickle import NONE


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.nodes = []

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.nodes.append(node.value)    

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
        self.nodes.remove(node.value)
        temp_node = node.next 
        node.value = temp_node.value
        node.next = temp_node.next
        temp_node.next = None
       

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

    linkedList1.deleteNode(node3)
    linkedList1.printAll()

        