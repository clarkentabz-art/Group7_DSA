from flask import Flask, render_template, request
from myqueue import Queue
from binaryTree import BinaryTree

app = Flask(__name__)

# --- Queue setup ---
order_queue = Queue() 

# --- Global course trees ---
courses = {
    "Learn how to sew": BinaryTree("Sewing"),
    "Learn how to draw": BinaryTree("Drawing"),
}

# Default course
default_course = "Learn how to sew"

# --- Routes ---
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

# Helper to convert tree to dict for template
def tree_to_dict(node):
    if node is None:
        return None
    return {
        'value': node.value,
        'left': tree_to_dict(node.left),
        'right': tree_to_dict(node.right)
    }

@app.route('/tree', methods=['GET', 'POST'])
def tree_page():
    result = ""
    
    # Default course when first loading the page
    selected_course = default_course  
    tree = courses[selected_course]

    if request.method == 'POST':
        clicked_course = request.form.get('course')
        if clicked_course in courses:
            selected_course = clicked_course
            tree = courses[selected_course]
            result = f"Showing tree for: {selected_course}"

    tree_dict = tree_to_dict(tree.root)

    return render_template(
        "tree.html",
        result=result,
        tree=tree_dict,
        courses=list(courses.keys()),
        selected_course=selected_course
    )

if __name__ == '__main__':
    app.run(debug=True)
