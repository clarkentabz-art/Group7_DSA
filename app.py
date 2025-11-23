from flask import Flask, render_template, request
from myqueue import Queue
from binaryTree import BinaryTree, Node
import json

app = Flask(__name__)

# --- Queue setup ---
order_queue = Queue() 

# --- Global course trees ---
courses = {
    "Learn how to sew": BinaryTree("Sewing"),
    "Learn how to draw": BinaryTree("Drawing"),
}

# Default course (can be None if you want no default)
default_course = None

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

# --- Helper functions ---
def tree_to_dict(node):
    if node is None:
        return None
    return {
        'value': node.value,
        'completed': getattr(node, 'completed', False),
        'left': tree_to_dict(node.left),
        'right': tree_to_dict(node.right)
    }

def gather_nodes_with_paths(node, path=None, out=None):
    if out is None:
        out = []
    if path is None:
        path = []
    if node is None:
        return out
    out.append((node.value, ''.join(path)))
    if node.left:
        gather_nodes_with_paths(node.left, path + ['L'], out=out)
    if node.right:
        gather_nodes_with_paths(node.right, path + ['R'], out=out)
    return out

# Keep track of last selected course to maintain state
last_selected_course = {'course': default_course}

@app.route('/tree', methods=['GET', 'POST'])
def tree_page():
    result = ""
    selected_course = last_selected_course['course']
    tree = courses.get(selected_course) if selected_course else None
    show_custom_panel = False

    if request.method == 'POST':
        # --- Delete course ---
        deleted = request.form.get("delete_course")
        if deleted and deleted in courses:
            del courses[deleted]
            result = f"Deleted course: {deleted}"
            selected_course = list(courses.keys())[0] if courses else None
            tree = courses.get(selected_course)
            last_selected_course['course'] = selected_course
            tree_dict = tree_to_dict(tree.root) if tree else None
            return render_template(
                "tree.html",
                result=result,
                tree=tree_dict,
                courses=list(courses.keys()),
                selected_course=selected_course,
                show_custom_panel=False,
                nodes_with_paths=gather_nodes_with_paths(tree.root) if tree else []
            )

        # --- Lock the tree ---
        lock_course = request.form.get("lock_course")
        if lock_course and lock_course in courses:
            courses[lock_course].locked = True
            result = f"Tree '{lock_course}' is now locked."
            tree = courses[lock_course]

        # --- Course selection ---
        clicked_course = request.form.get('course')
        if clicked_course and clicked_course in courses:
            selected_course = clicked_course
            tree = courses[selected_course]
            last_selected_course['course'] = selected_course

        # --- Show custom panel ---
        if "create_custom" in request.form:
            show_custom_panel = True

        # --- Save custom tree ---
        if "save_custom_tree" in request.form:
            root_goal = request.form.get("root_goal", "").strip()
            child_goal = request.form.get("child_goal", "").strip()

            if not root_goal:
                result = "Root goal is required."
            else:
                new_tree = BinaryTree(root_goal)
                if child_goal:
                    new_tree.insert_left(new_tree.root, child_goal)
                new_tree.locked = False
                courses[root_goal] = new_tree
                selected_course = root_goal
                tree = new_tree
                last_selected_course['course'] = root_goal
                show_custom_panel = True
                result = f"Custom course '{root_goal}' created successfully."

        # --- Insert node under existing node ---
        parent_path = request.form.get("parent_path")
        new_value = request.form.get("new_value", "").strip()
        side = request.form.get("side")
        if parent_path is not None and new_value and tree:
            parent_node = tree.find_by_path(list(parent_path))
            if parent_node:
                if side == "L":
                    tree.insert_left(parent_node, new_value)
                else:
                    tree.insert_right(parent_node, new_value)
                result = f"Added '{new_value}' under '{parent_node.value}' on {side} side."
                show_custom_panel = True

        # --- Toggle node completion ---
        toggle_path = request.form.get("toggle_path")
        if toggle_path and tree and not getattr(tree, "locked", False):
            node = tree.find_by_path(list(toggle_path))
            if node:
                node.completed = not node.completed

    tree_dict = tree_to_dict(tree.root) if tree else None
    nodes_with_paths = gather_nodes_with_paths(tree.root) if tree else []

    return render_template(
        "tree.html",
        result=result,
        tree=tree_dict,
        courses=list(courses.keys()),
        selected_course=selected_course,
        show_custom_panel=show_custom_panel,
        nodes_with_paths=nodes_with_paths
    )


if __name__ == '__main__':
    app.run(debug=True)
