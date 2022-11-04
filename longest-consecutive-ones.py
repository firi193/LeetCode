class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i,result,zero_count=0,0,0
        for j in range(len(nums)):
            if(nums[j]==0):
                zero_count=zero_count+1
            # print('zero',zero_count)
            while(zero_count>k):
                if(nums[i]==0):
                    zero_count-=1
                i+=1
            # print('i',i)
            # print(j)
            result=max(result,j-i+1)
            # print('res',result)
        return result
