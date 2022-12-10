# Write here the code challenge solution

# class TreeNode:
#     def__init__(self, val=0, left=None, right=None):

#         self.val = val
#         self.left = left
#         self.right = right

#     def findTarget(self, root: Optional)    

class Node:
    '''this function to create node'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right= None

class Tree:
    '''this function to create tree'''
    def __init__(self):
        self.root = None  

    def findTarget(self, k):
        if not self.root: return False
        bfs, s = [self.root], set()
        for i in bfs:
            if k - i.value in s: return True
            s.add(i.value)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False  


if __name__ =='__main__':
    tree=Tree()
    node1=Node(7)
    node2=Node(2)
    node3=Node(9)
    node4=Node(1)
    node5=Node(5)
    node6=Node(14)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    #node3.left = None
    node3.right = node6

    tree.root=node1
    tree.findTarget(3)

    result = tree.findTarget(3)
    print(result)