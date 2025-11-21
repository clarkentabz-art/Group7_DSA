class Node:
    """A node in a binary tree."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """A binary tree data structure."""
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert_left(self, current_node, value):
        """Insert a node as the left child of the current node."""
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value, left=current_node.left)
            current_node.left = new_node

    def insert_right(self, current_node, value):
        """Insert a node as the right child of the current node."""
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value, right=current_node.right)
            current_node.right = new_node

    def preorder_traversal(self, start, traversal=""):
        if start:
            traversal += str(start.value) + " "
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal.strip()

    def inorder_traversal(self, start, traversal=""):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.value) + " "
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal.strip()

    def postorder_traversal(self, start, traversal=""):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += str(start.value) + " "
        return traversal.strip()

    def search(self, root, key):
        """Return True if node exists, False otherwise."""
        nodes = self.inorder_traversal(root).split()
        return key in nodes

    def delete(self, root, key):
        """Delete a node using BFS (level-order delete). Return message."""
        if root is None:
            return "No tree exists."

        if root.value == key and root.left is None and root.right is None:
            self.root = None
            return f"Node '{key}' deleted. Tree is now empty."

        queue = [(root, None)]
        key_node = None
        deep = None
        deep_parent = None

        while queue:
            current, parent = queue.pop(0)
            deep = current
            deep_parent = parent

            if current.value == key:
                key_node = current

            if current.left:
                queue.append((current.left, current))
            if current.right:
                queue.append((current.right, current))

        if key_node is None:
            return f"Node '{key}' not found."

        key_node.value = deep.value

        if deep_parent:
            if deep_parent.left == deep:
                deep_parent.left = None
            else:
                deep_parent.right = None

        return f"Node '{key}' deleted."

# Optional: quick test if run standalone
if __name__ == "__main__":
    tree = BinaryTree("R")
    tree.insert_left(tree.root, "A")
    tree.insert_right(tree.root, "B")
    tree.insert_left(tree.root.left, "C")
    tree.insert_right(tree.root.left, "D")
    tree.insert_left(tree.root.right, "E")
    tree.insert_right(tree.root.right, "F")
    tree.insert_left(tree.root.right.right, "G")

    print("Preorder:", tree.preorder_traversal(tree.root))
    print("Inorder:", tree.inorder_traversal(tree.root))
    print("Postorder:", tree.postorder_traversal(tree.root))

    print("Search B:", tree.search(tree.root, "B"))
    print("Search Z:", tree.search(tree.root, "Z"))

    print(tree.delete(tree.root, "B"))
    print("Preorder after delete:", tree.preorder_traversal(tree.root))
