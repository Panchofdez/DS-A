class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self, traversal_type):
        """Print out all tree nodes
        as they are visited in
        a pre-order, inorder or post-order traversal"""
        answer = None
        if traversal_type.lower() == "preorder": 
            answer = self.preorder_print(self.root,[])
        elif traversal_type.lower() == "inorder":
            answer = self.inorder_print(self.root,[])
        elif traversal_type.lower() == "postorder":
            answer = self.postorder_print(self.root,[])
        return "-".join(list(map(str, answer)))

    def preorder_search(self, node, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if node.value == find_val:
            return True
        if node.left == None or node.right == None:
            return False
        else:
            found = self.preorder_search(node.left, find_val)
            if found == False:
                found = self.preorder_search(node.right, find_val)
        return found

    def preorder_print(self, node, traversal):
        """Helper method - use this to create a 
        recursive print solution. Using preorder traversal"""
        traversal.append(node.value)
        if node.left == None or node.right == None:
            return 
        else:
            self.preorder_print(node.left, traversal)
            self.preorder_print(node.right, traversal)
            
        return traversal
    def inorder_print(self,node, traversal):
        """using inorder traversal"""
        # if node.left:
        #     self.inorder_print(node.left, traversal)
        # traversal.append(node.value)
        # if node.right:
        #     self.inorder_print(node.right, traversal)
        # return traversal
        # or
        if node:
            self.inorder_print(node.left, traversal)
            traversal.append(node.value)
            self.inorder_print(node.right, traversal)
        return traversal
    def postorder_print(self, node, traversal):
        """Using post-order traversal"""
        if node:
            self.postorder_print(node.left, traversal)
            self.postorder_print(node.right, traversal)
            traversal.append(node.value)
        return traversal

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree("preorder"))

#Should be 4-2-5-1-3
print(tree.print_tree("inorder"))


#Should be 4-5-2-3-1
print(tree.print_tree("postorder"))

