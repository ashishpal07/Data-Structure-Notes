# find maximum & minimum and insert value from the BST


# A binary tree node has data, pointer to left child  
# and a pointer to right child  
class Node: 
    def __init__(self,data): 
        self.data = data 
        self.left = None
        self.right = None
  

# Function to insert a new node in BST 
def insert(root, data): 
  
    # 1. If the tree is empty, return a new,      
    # single node 
    if root == None:
        return Node(data) 
  
    # 2. Otherwise, recur down the tree 
    if data < root.data: 
        root.left = insert(root.left, data) 
    if data > root.data: 
        root.right = insert(root.right, data) 
      
    # return the (unchanged) node pointer 
    return root 


  
# Function to find the node with maximum value  
# i.e. rightmost leaf node  
def maxValue(root): 
    current = root 
      
    #loop down to find the rightmost leaf 
    while(current.right): 
        current = current.right 
    return current.data 



# Function to find the node with minimum value 
# i.e leftmost leaf node
def minValue(root):
    current = root
    
    # Loop down to find leftmost leaf
    while(current.left):
        current = current.left
    return current.data



def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
  
# Driver code  

root =  Node(50)
root = insert(root,2) 
root = insert(root,1) 
root = insert(root,3) 
root = insert(root,65)
root = insert(root,5) 

inorder(root)

print("Maximum value in BST is {}".format(maxValue(root)))
print("Minimum value in BST is {}".format(minValue(root)))
