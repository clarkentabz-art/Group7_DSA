from flask import Flask, render_template, request
from myqueue import Queue

app = Flask(__name__)

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

order_queue = Queue() 

@app.route('/queue', methods=['GET', 'POST'])
def queue_page():
    result = None
    if request.method == 'POST':
        order = request.form.get('order')
        if 'enterOrder' in request.form and order:
            code = order_queue.enqueue(order)
            result = f"Order added! Code: {code}"
        elif 'finishOrder' in request.form:
            served = order_queue.dequeue()
            if served:
                result = f"Served order {served['code']}"
            else:
                result = "Queue is empty!"

    return render_template('queue.html', queue=order_queue.display(), result=result)


if __name__ == '__main__':
    app.run(debug=True)
