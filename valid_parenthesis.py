class Solution(object):
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        arr=[]
        for i in range(len(s)):
            if s[i]=='(':
                if (s[i+1]==')'):
                    arr.append(True)
                else:
                    arr.append(False)
            if s[i]=='[':
                if (s[i+1]==']'):
                    arr.append(True)
                else:
                    arr.append(False)
            if s[i]=='{':
                if (s[i+1]=='}'):
                    arr.append(True)
                else:
                    arr.append(False)
            result = all(element == True for element in arr)
            if result==True:
                return True
            else:
                return False
