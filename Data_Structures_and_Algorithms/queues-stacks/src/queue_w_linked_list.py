# Implementing a queue using a Linked List as the underlying data structure

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, item):
        new_node = LinkedListNode(item)
        # check if queue is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node            # imagine an instantiated queue q
        else:                               # q.enqueue(node)
            # add new node to rear          # How would you know whether or not there's a rear
            self.rear.next = new_node       # to the queue? You would check if there was no queue at all;
            # reassign rear to new node     # As long as there was, you would refer to q.rear.
            self.rear = new_node            # You would say, q.rear.next = node   and   q.rear = node
    def dequeue(self):
        # check if queue is empty
        if self.front is not None:
            # keep copy of old front            #
            old_front = self.front              #  taking care of the queue
            # set new front                     #
            self.front = old_front.next         # 

        # check if the queue is now empty       #
        if self.front is None:                  # queue hygiene
            # make sure rear is also None       #
            self.rear = None                    #

        return old_front                        #  popping the dequeue'd item