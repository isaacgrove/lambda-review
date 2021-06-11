#
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBinaryTreeInvert(root):
    queue = []
    if root is None:
        return None
    queue.append(root)
    while len(queue) != 0:
        cur = queue.pop(0)
        holder = cur.left
        cur.left = cur.right
        cur.right = holder
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)
    return root