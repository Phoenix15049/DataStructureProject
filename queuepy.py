class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # True if queue is empty

    def isEmpty(self):
        return len(self.queue) == 0

    # Returns rear element of queue 

    def rear(self):
        return self.queue[0]
        
    # Returns front element of queue 
    
    def front(self):
        return self.queue[len(self.queue) - 1]

    
    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

#Examples

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()