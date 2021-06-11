#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isLeaf(node):
    if node.left is None and node.right is None:
        return True
    return False
    
def minimumDepthBinaryTree(root):
    a = 10000
    b = 10000
    if isLeaf(root):
        return 1
    if root.left:
        a = minimumDepthBinaryTree(root.left)
    if root.right:
        b = minimumDepthBinaryTree(root.right)
    return min(a, b) + 1