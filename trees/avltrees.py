#In avl trees the difference in height between left and right must always be <=1

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class AVL_Tree:
	def __init__(self):
		self.root = None
		self.size = 0

	def add(self, value):
		node = Node(value)
		new_root = self.add_helper(self.root, node)
		self.root = new_root
		self.preorder_print()
		print()
	def add_helper(self, parent, new_node):
		if parent == None:
			return new_node 
		if parent.value < new_node.value:
			parent.right = self.add_helper(parent.right, new_node)
			self.size +=1
		else:
			parent.left = self.add_helper(parent.left, new_node)
			self.size +=1
		new_parent = self.check_balance(parent)
		return new_parent

		
	def check_balance(self, node):
		if (self.height(node.left) - self.height(node.right) > 1) or (self.height(node.left) - self.height(node.right) < -1):
			node = self.rebalance(node)
		return node

	def rebalance(self, node):
		if self.height(node.left) - self.height(node.right) > 1:
			if self.height(node.left.left) > self.height(node.left.right):
				node = self.rightRotate(node)
			else:
				node = self.leftRightRotate(node)
		else: 
			if self.height(node.right.right) > self.height(node.right.left):
				node = self.leftRotate(node)
			else:
				node = self.rightLeftRotate(node)	
		return node	
	

	def height(self, node):
		if node == None:
			return 0
		left_height = self.height(node.left)
		right_height = self.height(node.right)
		if left_height > right_height:
			return left_height + 1 
		else:
			return right_height + 1

	def leftRotate(self, node):
		tmp = node.right
		node.right = tmp.left
		tmp.left = node 
		return tmp 

	def rightRotate(self, node):
		tmp = node.left
		node.left = tmp.right
		tmp.right = node 
		return tmp

	def rightLeftRotate(self, node):
		node.right = self.rightRotate(node.right)
		return self.leftRotate(node)

	def leftRightRotate(self, node):
		node.left = self.leftRotate(node.left)
		return self.rightRotate(node)

	def preorder_print(self):
		return self.preorder_traversal(self.root)

	def preorder_traversal(self, root):
		if root == None:
			return
		print("{0} ".format(root.value), end="")
		self.preorder_traversal(root.left)
		self.preorder_traversal(root.right)




# Python code to insert a node in AVL tree 
  
# Generic tree node class 
# class TreeNode(object): 
#     def __init__(self, val): 
#         self.val = val 
#         self.left = None
#         self.right = None
#         self.height = 1
  
# AVL tree class which supports the  
# Insert operation 
# class AVL_Tree(object): 
  
#     # Recursive function to insert key in  
#     # subtree rooted with node and returns 
#     # new root of subtree. 
#     def insert(self, root, key): 
      
#         # Step 1 - Perform normal BST 
#         if not root: 
#             return TreeNode(key) 
#         elif key < root.val: 
#             root.left = self.insert(root.left, key) 
#         else: 
#             root.right = self.insert(root.right, key) 
  
#         # Step 2 - Update the height of the  
#         # ancestor node 
#         root.height = 1 + max(self.getHeight(root.left), 
#                            self.getHeight(root.right)) 
  
#         # Step 3 - Get the balance factor 
#         balance = self.getBalance(root) 
  
#         # Step 4 - If the node is unbalanced,  
#         # then try out the 4 cases 
#         # Case 1 - Left Left 
#         if balance > 1 and key < root.left.val: 
#             return self.rightRotate(root) 
  
#         # Case 2 - Right Right 
#         if balance < -1 and key > root.right.val: 
#             return self.leftRotate(root) 
  
#         # Case 3 - Left Right 
#         if balance > 1 and key > root.left.val: 
#             root.left = self.leftRotate(root.left) 
#             return self.rightRotate(root) 
  
#         # Case 4 - Right Left 
#         if balance < -1 and key < root.right.val: 
#             root.right = self.rightRotate(root.right) 
#             return self.leftRotate(root) 
  
#         return root 
  
#     def leftRotate(self, z): 
  
#         y = z.right 
#         T2 = y.left 
  
#         # Perform rotation 
#         y.left = z 
#         z.right = T2 
  
#         # Update heights 
#         z.height = 1 + max(self.getHeight(z.left), 
#                          self.getHeight(z.right)) 
#         y.height = 1 + max(self.getHeight(y.left), 
#                          self.getHeight(y.right)) 
  
#         # Return the new root 
#         return y 
  
#     def rightRotate(self, z): 
  
#         y = z.left 
#         T3 = y.right 
  
#         # Perform rotation 
#         y.right = z 
#         z.left = T3 
  
#         # Update heights 
#         z.height = 1 + max(self.getHeight(z.left), 
#                         self.getHeight(z.right)) 
#         y.height = 1 + max(self.getHeight(y.left), 
#                         self.getHeight(y.right)) 
  
#         # Return the new root 
#         return y 
  
#     def getHeight(self, root): 
#         if not root: 
#             return 0
  
#         return root.height 
  
#     def getBalance(self, root): 
#         if not root: 
#             return 0
  
#         return self.getHeight(root.left) - self.getHeight(root.right) 
  
#     def preOrder(self, root): 
  
#         if not root: 
#             return
  
#         print("{0} ".format(root.val), end="") 
#         self.preOrder(root.left) 
#         self.preOrder(root.right) 
  
  
myTree = AVL_Tree() 

myTree.add(10)
myTree.add(20)
myTree.add(30)
myTree.add(40)
myTree.add(50)
myTree.add(25)

myTree.preorder_print()

# myTree = AVL_Tree() 
# root = None
  
# root = myTree.insert(root, 10) 
# root = myTree.insert(root, 20) 
# root = myTree.insert(root, 30) 
# root = myTree.insert(root, 40) 
# root = myTree.insert(root, 50) 
# root = myTree.insert(root, 25) 

# myTree.preOrder(root) 
# print() 