#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def max_depth(node):
    if node is None:
        return 0
        
    max_l = max_depth(node.left)
    max_r = max_depth(node.right)
    
    if max_l is False or max_r is False:
        # we've found an imbalanced subtree. Return it up.
        return False
    
    if abs(max_l - max_r) > 1:
        return False
    
    return max(max_l, max_r) + 1
 

def balancedBinaryTree(root):
    a = max_depth(root)
    if a is False:
        return False
    return TrueB