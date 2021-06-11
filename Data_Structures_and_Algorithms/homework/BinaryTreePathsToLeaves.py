
'''
Given a binary tree of integers, return all the paths from the tree's root 
to its leaves as an array of strings. The strings should have the 
following format:
"root->node1->node2->...->noden", representing the path from root to noden, 
where root is the value stored in the root and node1,node2,...,noden 
are the values stored in the 1st, 2nd,..., and nth nodes in the path 
respectively (noden representing the leaf).

'''
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
        
def recurse(node, res, path_str):
    if node is None:
        return None
    if isLeaf(node):
        path_str += str(node.value)
        res.append(path_str)
        return
    else:
        path_str += str(node.value) + '->'
    a = recurse(node.left, res, path_str)
    b = recurse(node.right, res, path_str)

def treePaths(t):
    results = []
    path_str = ''
    recurse(t, results, path_str)
    return results