class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # The main stack
        self.stack = []
        # The auxiliary stack to keep track of the minimum elements
        self.min_stack = []

    def push(self, val):
        """
        Pushes the element val onto the stack.
        """
        self.stack.append(val)
        # If min_stack is empty or val is less or equal than the top of min_stack, push val into min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        Removes the element on the top of the stack.
        """
        # If the popped element is the same as the top of min_stack, pop it from min_stack as well
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        """
        Gets the top element of the stack.
        """
        return self.stack[-1]

    def getMin(self):
        """
        Retrieves the minimum element in the stack.
        """
        return self.min_stack[-1]
#time O(1)
#space O(n)
