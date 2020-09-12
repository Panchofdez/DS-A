class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_helper(self.root, new_val)
    def search(self, find_val):
        return self.search_helper(self.root, find_val)
    def remove(self, val):
        return self.remove_helper(self.root, val)
    def print(self):
        answer = self.inorder_print(self.root,[])
        return "-".join(list(map(str, answer)))
        
    def search_helper(self, node, find_val):
        found = False
        if node == None:
            return False
        if node.value == find_val:
            found = True
        else:
            if find_val < node.value:
                found = self.search_helper(node.left, find_val) 
            elif find_val > node.value:
                found = self.search_helper(node.right, find_val)
        return found
    def insert_helper(self, node,new_val):
        if new_val < node.value:
            if node.left == None:
                node.left = Node(new_val)
                return
            else:
                self.insert_helper(node.left, new_val)
        elif new_val > node.value:
            if node.right == None:
                node.right = Node(new_val)
                return
            else:
                self.insert_helper(node.right, new_val)
    def remove_helper(self, node, val):
        if node:
            if val > node.value:
                node.right = self.remove_helper(node.right, val)
            elif val < node.value:
                node.left = self.remove_helper(node.left, val)
            else:
                if node.left is None:
                    temp =  node.right
                    node = None
                    return temp 
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp  
                else:
                    inorder_successor = self.find_min_node(node.right)
                    node.value = inorder_successor 
                    node.right = self.remove_helper(node.right, inorder_successor)
        return node
    def find_min_node(self, node):
        if node.left == None:
            return node.value
        else:
            return self.find_min_node(node.left)
    def inorder_print(self,node, traversal):
        """using inorder traversal"""
        if node:
            self.inorder_print(node.left, traversal)
            traversal.append(node.value)
            self.inorder_print(node.right, traversal)
        return traversal
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(7)
tree.insert(5)
tree.insert(9)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))


print(tree.print())
root = tree.remove(7)
print(tree.print())
print(tree.search(9))