class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        j=len(cardPoints)-k
        summ=0
        maxx=0
        summ=sum(cardPoints[j:])
        maxx=summ
        while(j<len(cardPoints)):
            summ=summ-cardPoints[j]+cardPoints[i]
            maxx=max(maxx,summ)
            i+=1
            j+=1
        return maxx
