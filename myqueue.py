import string

class Node:
    def __init__(self, order, code):
        self.order = order
        self.code = code
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.letter_index = 0
        self.number_counter = 1 

    def generate_code(self):
        letter = string.ascii_uppercase[self.letter_index]
        code = f"{letter}{self.number_counter:02d}"

        # Increment for next code
        self.number_counter += 1
        if self.number_counter > 99:
            self.number_counter = 1
            self.letter_index += 1
            if self.letter_index >= len(string.ascii_uppercase):
                self.letter_index = 0 

        return code

    def enqueue(self, order):
        code = self.generate_code()
        new_node = Node(order, code)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return code

    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return {'order': removed.order, 'code': removed.code}

    def display(self):
        current = self.head
        items = []
        while current:
            items.append({'order': current.order, 'code': current.code})
            current = current.next
        return items
