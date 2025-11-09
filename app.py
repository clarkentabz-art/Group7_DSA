from flask import Flask, render_template, request

app = Flask(__name__)

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
            return None
        else:
            current = self.head
            queue = []
            while current:
                queue.append(current.data)
                current = current.next
            list = (' '.join(queue))    
            return  list

cashier = Queue()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        operation = request.form.get('operation')
    return render_template('works.html', result=result)

@app.route('/queue', methods=['GET', 'POST'])
def queue():
    if request.method == "POST":
        data = str(request.form.get('order', ''))
        if not data:
            if request.form.get('finishOrder') == 'orderServed':
                cashier.dequeue()
                result = cashier.display()
                return render_template('queue.html', result=result)
            else: 
                result = cashier.display()
                return render_template('queue.html', result=result)
        elif request.form.get('enterOrder') == 'newOrder':
            cashier.enqueue(data)
            result = cashier.display()
            return render_template('queue.html', result=result)
        else:
            result = cashier.display()
            return render_template('queue.html', result=result)
    result = cashier.display()
    return render_template('queue.html', result=result), 

if __name__ == '__main__':
    app.run(debug=True)