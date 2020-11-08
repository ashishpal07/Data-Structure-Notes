# basic operations : enqueue(), dequeue(), peek()
#     enqueue - adding element into end of queue
#     dequeue - removing element from beagening of queue // FIFO
#     peek - return 1st ele without removing it 

# FIFO : first in first out


# implementation of queues

class Queue:
    def __init__(self):
        self.queue = []
        
    # empty or not
    def is_empty(self):
        self.queue == []
        
    #  enqueue()
    def enqueue(self, data):
        self.queue.append(data)
        
    #  dequeue() // O(N) use doubly linked list for these
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1
    
    def peek(self):
        if self.size_queue() == 0:
            return -1
        else:
            return self.queue[0]
    
    def size_queue(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(8)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print('size : %d' % queue.size_queue())
print('peek : %d' % queue.peek())
