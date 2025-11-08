class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return len(self) == 0

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
        current = self.head
        queue = []
        while current:
            queue.append(current.data)
            current = current.next
        return queue
    
#test ku lng

create_outfit = Queue()
create_outfit.enqueue("MiuMiu Headband")
create_outfit.enqueue("Tiffany & Co. Earrings")
create_outfit.dequeue()
create_outfit.enqueue("Gusi Belt")
print(create_outfit.display())
