# Linked List Fabulous programming to understand


# class node of linked list(initialize node object)
class Node:
    def __init__(self, data):
        self.data = data       # assign data
        self.next = None       # initialize next as null
        
        
        
        
# linked list class
class LinkedList:
    
    # function initialize head
    def __init__(self):
        self.head = None
    
    
    
    
    # insert new node at start of linked list ----> 4 step process 
    def insert_start(self, data):
        # add new node
        new_node = Node(data)
        
        # make next of new node as head
        new_node.next = self.head
        
        self.head = new_node
        
        
        
        
    # insert element at given point ----> 5 step process
    def insert_at_given_pt(self, prev_node, data):
        
        # check if previous node is exist
        if prev_node == None:
            return
        
        # create new node & put in the data
        new_node = Node(data)
        
        # 4. Make next of new Node as next of prev_node 
        new_node.next = prev_node.next
        
        # next of prev_node is new_node
        prev_node.next = new_node
    
    
    
    
    # Add note at the end          ------> 6 step process
    def insert_end(self, data):
        
        new_node = Node(data)
        
        # 4. If the Linked List is empty, then make the 
        #  new node as head 
        if self.head == None:
            self.head = new_node
            
        # else traverse till the last node
        temp = self.head
        while temp.next != None:
            temp = temp.next
            
        # 6. Change the next of last node 
        temp.next = new_node
        
    
    
    
    # delete node from linked list  -------> khud hi count krlo
    def delete_node(self, data):
        
        # store head node
        temp = self.head
        
        # If head node itself holds the data to be deleted
        if temp != None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
            
        # Search for the key to be deleted
        while temp != None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
            
        # if data is not present in linked list
        if temp == None:
            return
        
        prev.next = temp.next
        
        temp = None
                

        
        
        
        
    # function to print linked list starting from head
    def PrintList(self):
        temp = self.head
        
        while temp != None:
            print(temp.data)
            temp = temp.next
            
            
            
            
# start with empty list
list = LinkedList()
list.head = Node(1)
second = Node(2)
third = Node(3)

list.head.next = second
second.next = third

list.insert_start(12)
list.insert_at_given_pt(list.head.next,9)
list.insert_end(55)
list.delete_node(1)
list.PrintList()
