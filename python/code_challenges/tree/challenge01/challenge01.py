class Node:
    '''
    Creates a Binary tree node that has data,
    a pointer to it's left and right child
    '''
 
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

tree_array=[]
def pre_order(root):
    
    if root is not None:
        tree_array.append(root.value)
    if root.left is not None:
        pre_order(root.left)
    if root.right is not None:
        pre_order(root.right)
    return tree_array    


def binary_tree(root,pre_order,in_order):
    '''
    Takes two arrays (in-order + pre-order) to create a tree 
    and add nodes, to determine the new roots for each subnode
    '''

    if len(pre_order)==0 or  len(in_order)==0:
        return

    node = Node(pre_order[0])
    root = node

    index_in_order = in_order.index(node.value)

    node.left = binary_tree(root.left, pre_order[1:index_in_order + 1], in_order[:index_in_order])

    node.right = binary_tree(root.right, pre_order[index_in_order + 1:], in_order[index_in_order + 1:])
    return root


