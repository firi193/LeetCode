class MinStack(object):

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if val < 0:
            self.min = self.min - val
        

    def top(self):
        """
        :rtype: int
        """
        val = self.stack[-1]
        if val > 0:
            return val + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
