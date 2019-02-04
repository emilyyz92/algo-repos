import pdb

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_balanced(tree_root, depths = {'left': 0, 'right': 0}):
    # Determine if the tree is superbalanced
    # A tree is "superbalanced" if the difference
    # between the depths of any two leaf nodes is no greater than one.
    if not tree_root:
    	return depths
    elif not tree_root.left and not tree_root.right:
    	return depths
    else:
    	left = tree_root.left
    	right = tree_root.right
    	if left:
    		depths['left'] += 1
    	if right:
    		depths['right'] += 1
    	# pdb.set_trace()
    	return is_balanced(left, depths)
    	difference = abs(is_balanced(left) + left_depth - is_balanced(right) - right_depth)
    return difference
	
def return_result(tree_root):
	if is_balanced(tree_root) <= 1:
		return True
	else:
		return False

tree = BinaryTreeNode(1)
left = tree.insert_left(5)
right = tree.insert_right(9)
right_left = right.insert_left(8)
right.insert_right(5)
right_left.insert_left(7)
result = return_result(tree)
print(result)