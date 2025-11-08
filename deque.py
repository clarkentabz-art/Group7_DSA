class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, data):
        new_node = Node(data)
        if self.head: # if head is not empty then
            new_node.next = self.head
            self.head = new_node
        else: # if empty
            self.head = new_node
            self.tail = new_node

    def remove_front(self):
        if self.head is None:
            return None 

        removed_data = self.head.data
        self.head = self.head.next
        removed_data = None

    def add_rear(self, data):
        new_node = Node(data)
        if self.head: # if self.tail is not empty then
            self.tail.next = new_node
            self.tail = new_node
        else: # if head is empty
            self.head = new_node
            self.tail = new_node
            

    def remove_rear(self):
        if self.head is None:
            return None
        
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        
        current_node = self.head # Start at the head
        while current_node.next != self.tail: # the while loop will set the current_node to the node before the tail
            current_node = current_node.next

        removed_data = self.tail.data 
        self.tail = current_node
        self.tail.next = None
        return removed_data

    def peak_front(self):
        return self.head.data
    
    def peak_back(self):
        return self.tail.data