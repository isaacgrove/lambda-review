# takes in an array of requests, either "push x" or "pop" where x == int
# implement a queue using two stacks, returning an array of the popped values


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        if right.isEmpty():
             # move everything from left to right
            while not left.isEmpty():
                a = left.pop()
                right.push(a)
        return right.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans