class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for t in tokens:
            if t.isdigit():
                stack.append(t)
            else:
                if len(stack)==0:
                    break
                a=int(stack.pop())
                b=int(stack.pop())
                if t=='+':
                    c=b+a
                elif t=='-':
                    c=b-a
                elif t=='*':
                    c=b*a
                elif t=='/':
                    c=int(b/a)
                stack.append(str(c))
        return stack[0]
