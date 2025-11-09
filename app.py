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
        
        if 'enterOrder' in request.form:
            selected_items = {}
            for item_name in order_queue.MENU.keys():
                quantity = request.form.get(item_name, 0, type=int)
                if quantity > 0:
                    selected_items[item_name] = quantity
            
            if selected_items:
                order_details = order_queue.enqueue(selected_items)
                
                wait_mins, wait_secs = divmod(order_details['wait'], 60)
                result = f"Order {order_details['code']} added! Total: P{order_details['total']:.2f}. Est. wait: {int(wait_mins)}m {int(wait_secs)}s"
            else:
                result = "Please select at least one item."
                
        elif 'finishOrder' in request.form:
            served = order_queue.dequeue()
            if served:
                result = f"Served order {served['code']}"
            else:
                result = "Queue is empty!"
    
    return render_template(
        'queue.html', 
        queue=order_queue.display(), 
        result=result,
        menu=order_queue.MENU
    )


if __name__ == '__main__':
    app.run(debug=True)