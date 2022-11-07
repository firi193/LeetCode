class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        i=0
        j=0
        output=[]
        if_match={}
        while j<len(s):
            if len(if_match)==len(p):
                if 0 not in list(if_match.values()):
                    output.append(list(if_match.keys())[0])
                i+=1   
                j=i
                if_match.clear()
            if len(if_match)<len(p) and j<len(s):
                if s[j] in p and s[j] not in list(if_match.values()):
                    if_match[j]=s[j]
                else:
                    if_match[j]=0
            j+=1
        return output
