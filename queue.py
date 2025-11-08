class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node  
            self.tail = new_node
            return
        else:
            self.tail.next = new_node  
            self.tail = new_node

    def dequeue(self):
            current = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return current.data

    def display(self):
        if self.head is None:
            return "Queue is empty."
        else:
            current = self.head
            queue = []
            while current:
                queue.append(current.data)
                current = current.next
            return queue
    
#test ku lng
cashier = Queue()
cashier.enqueue("Aliah")
cashier.enqueue("Joyce")
cashier.dequeue()
cashier.enqueue("Basta")
print(cashier.display())
