class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        dictt= {}
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                j = stk.pop()
                dictt[i], dictt[j] = j, i
        result = []
        i, d = 0, 1
        while i < len(s):
            if i in dictt:
                i = dictt[i]
                d *= -1
            else:
                result.append(s[i])
            i += d
            res="".join(result)
        return res
