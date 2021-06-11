# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

#
# This is a leetcode hard problem that was on our homework.
# This recursive solution works. I'd like to study it more in depth.
#
# Reverse linked list nodes k at a time, leaving remainder nodes alone if applicable
#
def reverse(a,b):
    '''Building block for recursion; reverses [a,b)'''
    pre = None
    cur = a
    nxt = a
    # as long as we're not at the end
    while cur != b:
        # anchor
        nxt = cur.next
        # reverse
        cur.next = pre
        # move pointers
        pre = cur
        cur = nxt
    return pre

def reverseNodesInKGroups(l, k):
    '''Recursively splits the job into reversing [a,b) and [b,k]'''
    # If there is no ll return nothing
    if l == None:
        return None
    # Point 3 pointers at the head - a, b, and l.
    # We will slide b along, k times, while leaving a in place.
    # a stays equal to the first argument of the function call - l the first time, b later on
    b = l
    a = b
    for i in range(k):
        # if b ever points at nothing, just return the head
        # (This is how we know there aren't k more elements)
        if b == None:
            return l
        b = b.next
    new_head = reverse(a,b)

    a.next = reverseNodesInKGroups(b,k)
    return new_head