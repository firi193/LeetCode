class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            current=nums[i]
            j=i-1
            while(j>=0 and nums[j]>current):
              nums[j+1]=nums[j]
              j=j-1
            nums[j+1]=current
        return nums
