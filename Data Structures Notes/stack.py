# their are three things which are as follows(stack)

# 1. push()
#       it pushes element in stack one by one like -
#       56,67,78,89  as on.
# 2. pop()
#       it removes last element of stack.
# 3. peek()
#       it returns the value of last element in the stack
#       without removing to it.


# implimentation of stack


#  LIFO : - last item we insert first item out.

class stack:
    def __init__(self):
        self.stack = []
        
    #  insert element to the stack // O(1)
    def push(self, data):
        self.stack.append(data)
        
    #  remove and return the last value (LIFO) // O(1)
    def pop(self):
        
        #  don't pop if stack is empty
        if self.stack_size() < 1:
            return -1
        
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    #  peek : it returns last element without removing it // O(1)
    def peek(self):
        return self.stack[-1]
    
    #  if list is empty // O(1)
    def is_empty(self):
        return self.stack == []
    
    #  stack size
    def stack_size(self):
        return len(self.stack)
    
# class object
stack = stack()
stack.push(1)
stack.push(12)
stack.push(3)
stack.push(8)
print('size : %d' % stack.stack_size())
print('pop : %d' % stack.pop())
print('peek : %d' % stack.peek())
print('size : %d' % stack.stack_size())
