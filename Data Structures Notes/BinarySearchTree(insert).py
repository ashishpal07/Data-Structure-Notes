#  BINARY SEARCH TREE(BST) INSERT VALUE OPERATION

# Class reprents the individual Node of BST
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.val = data

# Function to insert new node with the given key
def insert(root, data):
    
    if root == None:
        return Node(data)

    else:
        if root.val == data:
            return root

        elif root.val < data:
            root.right = insert(root.right, data)

        elif root.val > data:
            root.left = insert(root.left, data)

    return root


# Function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Main program to test the above functions

# Let us create the following BST 
#          50 
#         /  \ 
#       30    70 
#      /  \  /  \ 
#    20   40 60  80

r = Node(50)
r = insert(r, 80)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder

inorder(r)
