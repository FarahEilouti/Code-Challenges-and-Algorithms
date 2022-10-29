# Write here the code challenge solution
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
        '''
        defining the first
        component of the linked list
        '''
        self.head = None

    def append(self, value):
        '''
        funcion that adds values based on
        a condition of availability (not being none)
        '''
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node


    def delete_nth(self, n):
        '''
        function that is responsible of deleting
        a specific node starting from the end of the linkedlist
        '''
        
        counter = 1

        current = self.head
        while current.next is not None:
            counter += 1
            current = current.next
        
        # length of self = counter

        if 1 <= counter <= 30 and 1 <= n <= counter:
            position_to_delete = counter - n + 1

            pointer = self.head
            new_counter = 1
            while pointer is not None:
                if new_counter == position_to_delete - 1:
                    pointer.next = pointer.next.next
                new_counter += 1
                pointer = pointer.next
        else:
            print("Sorry, the length of list or your n value is out of range")

    def print(self):
        '''
        print function, and where we store 
        the list after deletion
        '''
        my_nodes = []
        current = self.head
        while current is not None:
            my_nodes.append(current.value)
            current = current.next
        # print(my_nodes)

        return my_nodes


       

if __name__ == "__main__":

    linkedList1 = LinkedList()

    linkedList1.append('a')
    linkedList1.append('b')
    linkedList1.append('c')
    linkedList1.append('d')
    linkedList1.append('e')

    print(linkedList1.print())
    linkedList1.delete_nth(3)
    print(linkedList1.print())
    

    
