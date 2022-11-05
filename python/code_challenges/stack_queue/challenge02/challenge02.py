# Write here the code challenge solution
from ast import Delete
from inspect import stack
from xml.dom.pulldom import CHARACTERS

class Node:
    def __init__(self,value):
        self.next = None
        self.value = value


class Stack:
    '''
    defining stack 
    elements and actions
    '''

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

    def print_all(self):

        if self.top is None:
            print("The stack is empty")
        else:
            while self.top is not None:
                print(self.top.value)
                self.pop()



def is_valid(string):
    '''
    1. defining a function called is_valid, we create an object from the class Stack.
    2. create a dictionary containing keys and values of the parenthesis (key = closed/ value = opened)
    3. looping into characters with a condition; 
    a. pushing the values into a new stack
    b. for the keys, if their specific values are on top of that new stack; let those values pop  

    4. The condition will result "True" because "each opening parenthesis' has found a closing one " otherwise it'll output "False"
    '''
    
    stack1 = Stack()

    lookup = {
        ')': '(', 
        '}': '{', 
        ']': '['
        }
    

    for character in string:

        if character in lookup.values():
            stack1.push(character)
        elif not stack1.is_empty() and lookup[character] == stack1.peek():
            stack1.pop()
        else:
            return False

    return stack1.is_empty()



if __name__ == '__main__':

   result = is_valid(string="()")
   print(result)
   
    # test_stack = Stack()

    # test_stack.push(2)
    # test_stack.push(3)
    # test_stack.push(4)
    # test_stack.push(5)

    # test_stack.print_all()
    