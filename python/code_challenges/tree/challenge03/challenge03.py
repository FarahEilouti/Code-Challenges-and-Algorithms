
class Node:
    
    def __init__(self, value):
        """
        Creating node components
        """
        self.value = value
        self.left = None
        self.right= None

class Tree:
    

    def __init__(self):
        """
        Creating Tree components
        """
        self.root = None
        self.pre_order_array=[]


    def convert_to_BST(self,arr=[]):
        """
        Given an integer array nums,
        convert it to a height-balanced
        binary search tree.
        """

        if not arr :
            return None
        arr.sort()
        mid = len(arr)//2
        root = Node(arr[mid])
        self.pre_order_array.append(root.value)
        root.left = self.convert_to_BST(arr[:mid])
        root.right = self.convert_to_BST(arr[mid+1:])
    
        return root

tree = Tree()
array = [5, 6, 4 , 3]
tree.convert_to_BST(array)
print(tree.pre_order_array)