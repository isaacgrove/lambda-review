#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    

def binaryTreePreOrderTraversal(root):
    # recursive or iterative
    # in order --> left, visit, right
    results = []
    stack = []
    stack.append(root)
    while len(stack) != 0:
        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
        
        if node.left is not None:
            stack.append(node.left)
            
        results.append(node.value)
        
    return results



def binaryTreeInOrderTraversal(root):
    # recursive or iterative
    # in order --> left, visit, right
    results = []
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        popped = stack.pop()
        results.append(popped.value)
        node = popped.right
        
    return results

a = Tree(5)
a.left = Tree(10)
a.right = Tree(15)
a.left.left = Tree(2)
a.left.right = Tree(4)
a.right.left = Tree(6)
a.right.right = Tree(8)

print(binaryTreePreOrderTraversal(a))
print(binaryTreeInOrderTraversal(a))