class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        list_words=[None]*len(words)
        for word in words:
            for letter in word:
                if(letter.isdigit()):
                    list_words[int(letter)-1]=word.replace(letter,'')   
        sentence=' '.join(list_words)
        return sentence
