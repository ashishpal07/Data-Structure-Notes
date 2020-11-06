# Python program to demonstrate delete operation 
# in binary search tree 
  
# A Binary Tree Node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
  
# A utility function to do inorder traversal of BST 
def inorder(root): 
    if root != None: 
        inorder(root.left) 
        print(root.data) 
        inorder(root.right) 
  

  
# A utility function to insert a new node with given key in BST 
def insert(root, data): 
  
    # If the tree is empty, return a new node 
    if root == None: 
        return Node(data) 
  
    # Otherwise recur down the tree 
    if data < root.data: 
        root.left = insert(root.left, data) 
    else: 
        root.right = insert(root.right, data) 
  
    # return the (unchanged) node pointer 
    return root 


  
# Given a non-empty binary search tree, return the node 
# with min data value found in that tree.
# entire tree does not need to be searched  
def minValueNode(root): 
    current = root
  
    # loop down to find the leftmost leaf 
    while(current.left != None): 
        current = current.left  
  
    return current  


  
# Given a binary search tree and a data, this function 
# delete the data and returns the new root 
def deleteNode(root, data): 
  
    # Base Case 
    if root == None: 
        return root  
  
    # If the data to be deleted is smaller than the root's 
    # data then it lies in  left subtree 
    if data < root.data: 
        root.left = deleteNode(root.left, data) 
  
    # If the data to be delete is greater than the root's data 
    # then it lies in right subtree 
    elif(data > root.data): 
        root.right = deleteNode(root.right, data) 
  
    # If data is same as root's data, then this is the node 
    # to be deleted 
    else: 
          
        # Node with only one child or no child 
        if root.left == None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right == None : 
            temp = root.left  
            root = None
            return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.data = temp.data 
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.data) 
  
  
    return root  
  
# Driver program to test above functions

""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 """
  

root = None
root = insert(root, 50) 
root = insert(root, 30) 
root = insert(root, 20) 
root = insert(root, 40) 
root = insert(root, 70) 
root = insert(root, 60) 
root = insert(root, 80) 
inorder(root)
print('------------------')
root = deleteNode(root, 40)
inorder(root)
