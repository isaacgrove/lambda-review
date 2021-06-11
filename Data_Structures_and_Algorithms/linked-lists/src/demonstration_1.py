"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class ListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

#
###starter code for this file
##
# def delete_node(node_to_delete):
#     # Your code here
# delete_node(y)

x = ListNode(4)
y = ListNode(10)
z = ListNode(15)
x.next = y
y.next = z


### hijacking the file for homework
#
# given a monotonically increasing linked list l (with head l), insert value
def insertValueIntoSortedLinkedList(l, value):
    ins = ListNode(value)
    current = l
    if l:
        if ins.value < l.value:
            # replace the head
            ins.next = l
            return ins
        while current.next:
            # exhausts at the end of the ll
            if ins.value < current.next.value:
                ins.next = current.next
                current.next = ins
                return l
            current = current.next
        current.next = ins
        return l
    else:
        l = ins
        return l
# Notes: in order, the flow of logic  
# 1) checks if there's a head (if not, return ins)
# 2) checks if the head needs replaced with ins (in the event ins is smaller than the entire list)
# 3) traverses the list, handling 2 cases: no current.next, meaning we've found the 
# end of the list and need only tack on ins, or ins.value < current.next.value, in which case it's time
# to unhook the list, insert ins, and rehook.
#
# Note how it does the while n times and the head checks once each, but two cases go into each n check
# (because the end could be anywhere)


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    # O(n + m) time
    # Merge two monotonically increasing ll's
    #
    # #main code assumes l1 and l2
    # --> handle situations where either runs out (while .next)
    # take min(current1.next, current2.next)
    # if l1 and l2:
    #     if l1.value < l2.value:
    #         base = l1
    #         feeder = l2
    #     else:
    #         base = l2
    #         feeder = l1
    #     # Now we're ready to do n + m while loop comparisons.
    #     anchor = None
    #     slider = base
    #     while slider.next and feeder:
    #         if feeder.value < slider.next.value:
    #             anchor = feeder.next
    #             feeder.next = slider.next
    #             slider.next = feeder
    #             feeder = anchor
    #         else:
    #             slider = slider.next
    #     # hook up the rest of the remaining list, return head
    #     # we either ran out of feeder or base.
    #     if not slider.next:
    #         slider.next = feeder
    #         return base
    #     # if there is no slider.next, slider.next = feeder, return base
    #     return base
    # if l1:
    #     return l1
    # if l2:
    #     return l2
    # return []