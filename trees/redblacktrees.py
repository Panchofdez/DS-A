#My implementation of redblack trees
#Red-Black Tree is a self-balancing Binary Search Tree (BST) where every node follows following rules
#every node is either red or black
#root is black
#nulls are black
#no two consecutive red nodes
#Every path from a node (including root) to any of its descendant NULL node has the same number of black nodes.
#black aunt: rotate
#red aunt: color flip
class Node:
	def __init__(self, value):
		self.value = value
		self.isBlack = False
		self.isLeftChild = False
		self.left = None
		self.right = None 
		self.parent = None

class RedBlackTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def add(self, value):
		node = Node(value)
		if self.root == None:
			self.root = node
			self.root.isBlack = True
			self.size += 1
			return
		else:
			self.add_helper(self.root, node)
			self.size += 1
			self.checkColor(node)
			self.root.isBlack = True
			self.checkBlackNodes(self.root)
			self.preorder_print()
			print()
	def add_helper(self, parent, new_node):
		if parent.value < new_node.value:
			if parent.right == None:
				parent.right = new_node
				new_node.isLeftChild = False
				new_node.parent = parent
				return
			else:
				return self.add_helper(parent.right, new_node)
		else:
			if parent.left == None:
				parent.left = new_node
				new_node.isLeftChild = True
				new_node.parent = parent
				return 
			else:
				return self.add_helper(parent.left, new_node)
	
	def checkColor(self, node):
		if node == self.root:
			return 
		print(node.value)
		print("Is Black", node.isBlack)
		print("Parent is Black", node.parent.isBlack)
		if node.isBlack == False and node.parent.isBlack == False:
			print("2 consecutive Red")
			self.correctTree(node)
		self.checkColor(node.parent)

	def correctTree(self, node):
		if node.parent.parent == None:
			return
		if node.parent.isLeftChild:
			if node.parent.parent.right == None or node.parent.parent.right.isBlack:
				return self.rotate(node)
			else:
				#here we do logic for colorflip if aunt is red
				print("colorflip")
				if node.parent.parent.right != None:
					node.parent.parent.right.isBlack = True
				node.parent.parent.isBlack = False
				node.parent.isBlack = True
				return 
		else:
			if node.parent.parent.left == None or node.parent.parent.left.isBlack:
				return self.rotate(node)
			else:
				#colorflip if aunt is red
				print("colorflip")
				if node.parent.parent.left != None:
					node.parent.parent.left.isBlack = True
				node.parent.parent.isBlack = False
				node.parent.isBlack = True
				return 

	def rotate(self, node):
		if node.isLeftChild:
			if node.parent.isLeftChild:
				print("Right Rotate")
				self.rightRotate(node.parent.parent)
				node.isBlack = False
				node.parent.isBlack = True
				if node.parent.right != None:
					node.parent.right.isBlack = False
			else:
				print("Right Left Rotate")
				self.rightLeftRotate(node.parent.parent)
				node.isBlack = True
				node.right.isBlack = False
				node.left.isBlack = False
		else:
			if node.parent.isLeftChild == False:
				print("Left Rotate")
				self.leftRotate(node.parent.parent)
				node.isBlack = False
				node.parent.isBlack = True
				if node.parent.left != None:
					node.parent.left.isBlack = False
			else:
				print("Left Right Rotate")
				self.leftRightRotate(node.parent.parent)
				node.isBlack = True
				node.right.isBlack = False
				node.left.isBlack = False

	def rightRotate(self, node):
		tmp = node.left
		node.left = tmp.right
		if node.left != None:
			node.left.parent = node
			node.left.parent.isLeftChild = True
		if node.parent == None:
			self.root = tmp 
			self.root.isBlack = True
			tmp.parent = None
		else:
			tmp.parent = node.parent
			if node.isLeftChild:
				tmp.parent.left = tmp
				tmp.isLeftChild = True 
			else:
				tmp.parent.right = tmp
				tmp.isLeftChild = False
		tmp.right = node
		node.isLeftChild = False
		node.parent = tmp

	def leftRotate(self, node):
		tmp = node.right
		node.right = tmp.left
		if node.right != None:
			node.right.parent = node
			node.right.isLeftChild = False
		if node.parent == None:
			self.root = tmp
			self.root.isBlack = True
			tmp.parent = None
		else:
			tmp.parent = node.parent
			if node.isLeftChild:
				tmp.parent.left = tmp
				tmp.isLeftChild = True
			else:
				tmp.parent.right = tmp
				tmp.isLeftChild = False
		tmp.left = node
		node.isLeftChild = True
		node.parent = tmp

	def rightLeftRotate(self, node):
		self.rightRotate(node.right)
		self.leftRotate(node)

	def leftRightRotate(self, node):
		self.leftRotate(node.left)
		self.rightRotate(node)

	def height(self,start_node):
		if self.root == None:
			return 0
		if start_node == None:
			return 0
		height_left = self.height(start_node.left) + 1
		height_right = self.height(start_node.right) + 1

		if height_left > height_right:
			return height_left
		else:
			return height_right

	def checkBlackNodes(self, node):
		if node == None:
			return 1
		rightblackNodes =  self.checkBlackNodes(node.right)
		leftblackNodes = self.checkBlackNodes(node.left)

		if rightblackNodes != leftblackNodes:
			print("Error return")
			self.checkColor(node)
		if node.isBlack == True:
			rightblackNodes += 1
		return rightblackNodes

	def preorder_print(self):
		return self.preorder_traversal(self.root)

	def preorder_traversal(self, root):
		if root == None:
			return
		print("{0} {1} ".format(root.value, root.isBlack), end="")
		self.preorder_traversal(root.left)
		self.preorder_traversal(root.right)


rbtree = RedBlackTree()

rbtree.add(3)
rbtree.add(1)
rbtree.add(5)
rbtree.add(7)
rbtree.add(6)
rbtree.add(8)
rbtree.add(9)
rbtree.add(10)

