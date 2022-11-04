class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=0
        maxi=0
        longest_sub=''
        while(i<len(s)):
            c=s[i]
            while c in longest_sub:
                longest_sub=longest_sub.replace(s[j],'')
                
                j=j+1
            longest_sub=longest_sub+c
            maxi=max(maxi, i-j+1)
            i+=1
        return maxi
