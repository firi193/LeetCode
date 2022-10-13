class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (1 <= i < len(nums) - 1) and nums[i]==(nums[i-1]+nums[i+1])/2:
                temp=nums[i+1]
                nums[i+1]=nums[-i+2]
                nums[-i+2]=temp
        return nums  
