
from cgitb import reset


class Node:
    def __init__(self, value):
        '''
        initializing and defining the 
        components of a linked list( object and its value)
        '''
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node
   

    def middle_node(self):
        counter = 1

        current = self.head
        while current.next is not None:
            counter += 1
            current = current.next
        
        # length of self = counter

        # middle node position = counter / 2
        import math  

        middle_position = math.ceil(counter / 2)

        result = []

        new_counter = 1

        pointer = self.head
        while pointer is not None:
            if new_counter >= middle_position:
                result.append(pointer.value)
            
            new_counter += 1
            pointer = pointer.next
        
        return result
       

if __name__ == "__main__":

    linkedList1 = LinkedList()

    linkedList1.append('a')
    linkedList1.append('b')
    linkedList1.append('c')
    linkedList1.append('d')
    linkedList1.append('e')

    result = linkedList1.middle_node()
    print(result)

    
