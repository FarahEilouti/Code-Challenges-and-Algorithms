# Write here the code challenge solution
from ast import Delete

class Node:
    def __init__(self,value):
        self.next = None
        self.value = value


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if not self.rear: # if the queue empty
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):

        if self.front == None:
            return("This queue is empty")        
        if self.front == self.rear:
            self.rear = None
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.front == None:
            return("This queue is empty")        
        return self.front.value



class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

# ---------------------------------------------

class MyQueue(object):

    def __init__(self):
        self.s1 = [] 
        self.s2 = [] 

    def push(self, x):
        '''
        Push element x to the back of queue
        '''
        while self.s1: 
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())


    def pop(self):
        '''
        Remove the element from the front
        '''
        self.peek()
        return self.s1.pop()

	
    def peek(self):
        '''
        Returns the element at the front of the queue
        '''
        return self.s1[-1]

    def empty(self):
        return not self.s1


if __name__ == "__main__":
    
    myqueue = MyQueue()

    myqueue.push(1)
    myqueue.push(2)
    myqueue.push(3)

    print(myqueue.peek())
    print(myqueue.pop())
    print(myqueue.empty())


# #using queue:
# queue1 = Queue()

# queue1.enqueue(10)
# queue1.enqueue(20)
# queue1.enqueue(30)

# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())



# # using stack
# stack1  = Stack()
# stack1.push("A")
# stack1.push("B")
# stack1.push("C")
# stack1.push("D")
# stack1.push("E")

# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.peek())
# # print(stack1.get_size())

