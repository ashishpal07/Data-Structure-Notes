# find the height of Binary Search Tree(BST)

# initialization of node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxHeight(node):
    if node == None:
        return -1

    # find height of each subtree(right/left) side
    else:
        rHeight = maxHeight(node.right)
        lHeight = maxHeight(node.left)

        if rHeight > lHeight:
            return rHeight + 1
        else:
            return lHeight + 1

# main program to derive code

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print("Height of tree is %d" %(maxHeight(root))) 


        
    
