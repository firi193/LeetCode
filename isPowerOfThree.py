class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def isPowerOfThree(n):
            if (n <= 0):
                return False
            if (n % 3 == 0):
                return isPowerOfThree(n//3)
            if (n == 1):
                return True
            return False
