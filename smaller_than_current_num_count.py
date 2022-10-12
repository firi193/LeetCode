class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        for num in nums:
            count=0
            for n in nums:
                if n<num:
                    count=count+1
            output.append(count)
        return output
