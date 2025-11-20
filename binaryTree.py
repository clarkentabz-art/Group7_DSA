class Node:
    """A node in a binary tree."""
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """A binary tree data structure."""
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert_left(self, current_node, value):
        """Insert a node as the left child of the current node."""
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        """Insert a node as the right child of the current node."""
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def preorder_traversal(self, start,traversal):
        """Traverse the tree in preorder (root, left, right)."""
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left,traversal)
            traversal = self.preorder_traversal(start.right,traversal)
        return traversal    

    def inorder_traversal(self, start,traversal):
        """Traverse the tree in inorder (left, root, right)."""
        if start:
            traversal = self.inorder_traversal(start.left,traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right,traversal)
        return traversal    

    def postorder_traversal(self, start, traversal):
        """Traverse the tree in postorder (left, right, root)."""
        if start:
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right,traversal)
            traversal += (str(start.value) + " ")
        return traversal   
    
    def search(self, root, key):
        value = root.value
        searched = self.inorder_traversal(root, "")
        if key in searched:
            return print(f"We have found your Node under the {self.root.value} Tree")
        else:
            return print(f"Sorry the Node you entered was not found under the {self.root.value} Tree, Try another Node or another Tree to search")
        
    def delete(self, root, key):
        if root is None:
            print("No tree hre!")
            return None
        
        if root.value == key and root.left is None and root.right is None:
            print(f"Node {key} deleted.")
            return None
        
        #BFS traversal para sa last/deepest node'd
        queue = [root]
        key_node = None
        deep = None
        deep_parent = None

        while queue:
            current = queue.pop(0)
            if current.value == key:
                key_node = current 
            deep = current
            if current.left: 
                deep_parent = current
                queue.append(current.left)
            if current.right:
                deep_parent = current
                queue.append(current.right)

        key_node.value = deep.value

        if key_node is None:
            print(f"Node {key} not found.")
            return root

        if deep_parent.right == deep:
            deep_parent.right = None
            print(f"Node {key} deleted.")
        else:
            deep_parent.left = None
            print(f"Node {key} deleted.")


if __name__ == "__main__":
   
    tree = BinaryTree("R")
    
    # Insert nodes
    tree.insert_left(tree.root, "A")
    tree.insert_right(tree.root, "B")
    tree.insert_left(tree.root.left, "C")
    tree.insert_right(tree.root.left, "D")
    tree.insert_left(tree.root.right, "E")
    tree.insert_right(tree.root.right, "F")
    tree.insert_left(tree.root.right.right, "G")
    
    print()

    print("Preorder traversal: " + tree.preorder_traversal(tree.root,""))
    ##tree.preorder_traversal(tree.root,"")
    print("\n\nInorder traversal: " + tree.inorder_traversal(tree.root,""))
    # tree.inorder_traversal(tree.root)
    print("\n\nPostorder traversal: " + tree.postorder_traversal(tree.root,""))
    # tree.postorder_traversal(tree.root)

    print("\n")

    #tree search test
    tree.search(tree.root, "B")
    tree.search(tree.root, "G")
    tree.search(tree.root, "Z")
    tree.delete(tree.root, "B")
    tree.search(tree.root, "B")

    print()


        
