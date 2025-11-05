from flask import Flask, render_template, request
from linkedlist import LinkedList

app = Flask(__name__)

# 🌸 Initialize the linked list
linked_list = LinkedList()

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

@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    result = ""
    
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')

        if action == 'insert_beginning':
            result = linked_list.insert_at_beginning(value)
        elif action == 'insert_end':
            result = linked_list.insert_at_end(value)
        elif action == 'remove_beginning':
            result = linked_list.remove_beginning()
        elif action == 'remove_end':
            result = linked_list.remove_end()
        elif action == 'remove_value':
            result = linked_list.remove_value(value)
        elif action == 'search':
            result = linked_list.search(value)

    list_state = linked_list.display()

    return render_template('linkedlist.html', result=result, list_state=list_state)


if __name__ == '__main__':
    app.run(debug=True)