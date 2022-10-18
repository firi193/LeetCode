class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1, n2 = 0, 1
        count = 0
        while count < n:
            nth = n1 + n2
           # update values
            n1 = n2
            n2 = nth
            count += 1
        return n1
