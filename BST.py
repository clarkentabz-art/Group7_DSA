class Node:
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data < node.value:
                node.left = self.insert(node.left, data)
            elif data > node.value:
                node.right = self.insert(node.right, data)
        return node

    def get_min_value(self, node):
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def preorder_traversal(self, start,traversal):
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left,traversal)
            traversal = self.preorder_traversal(start.right,traversal)
        return traversal    

    def inorder_traversal(self, start,traversal):
        if start:
            traversal = self.inorder_traversal(start.left,traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right,traversal)
        return traversal    

    def postorder_traversal(self, start,traversal):
        if start:
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right,traversal)
            traversal += (str(start.value) + " ")
        return traversal
    
    def search(self, node, target):
        return None
        
    def delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp_val = self.get_min_value(node.right)
                node.value = temp_val
                node.right = self.delete(node.right, temp_val)
        return node
        
    def get_max_value(self, node):
        if node is None:
            return None
        current = node
        while current.right is not None:
            current = current.right
        return current.value
    
    def find_height(self, node):
        return
    

#TESTING
if __name__ == "__main__":
   
    test = BinarySearchTree()

    #Testing Insert
    test.root = test.insert(test.root, 10)
    test.root = test.insert(test.root, 20)
    test.root = test.insert(test.root, 11)
    test.root = test.insert(test.root, 35)
    test.root = test.insert(test.root, 83)
    test.root = test.insert(test.root, 7)
    test.root = test.insert(test.root, 100)

    #testing traversal
    print("Inorder traversal:", test.inorder_traversal(test.root,""))
    print("Preorder traversal:", test.preorder_traversal(test.root,""))
    print("Postorder traversal:", test.postorder_traversal(test.root,""))

    #testing getting min
    print("Minimum value:", test.get_min_value(test.root))
    print("Maximum value:", test.get_max_value(test.root))

    #testing delete node
    print("Inorder before delete:", test.inorder_traversal(test.root,""))
    print("Preorder before delete:", test.preorder_traversal(test.root,""))
    print("Postorder before delete:", test.postorder_traversal(test.root,""))
    test.root = test.delete(test.root, 20)
    print("Inorder after deleting 20:", test.inorder_traversal(test.root,""))
    print("Preorder after deleting 20:", test.preorder_traversal(test.root,""))
    print("Postorder after deleting 20:", test.postorder_traversal(test.root,""))
