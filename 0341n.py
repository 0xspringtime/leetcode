#stack
class NestedIterator:
    def __init__(self, nestedList):
        # The list is reversed and put into a stack
        self.stack = nestedList[::-1]

    def next(self):
        # We're guaranteed that the top of the stack is an integer,
        # so we just pop and return it.
        return self.stack.pop()

    def hasNext(self):
        # Check the top of the stack. If it's a list, unpack it (in reverse order)
        # and put the items back onto the stack.
        while self.stack:
            top = self.stack[-1]
            if isinstance(top, list):
                self.stack = self.stack[:-1] + top[::-1]
            else:
                return True

        return False
#time O(n)
#space O(n)
