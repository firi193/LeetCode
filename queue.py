from collections import deque
class MyQueue(object):

    def __init__(self):
        self.queue=deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()
        

    def peek(self):
        """
        :rtype: int
        """
        
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
