class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        answer=[]
        for i in range(len(l)):
            sub_nums=nums[l[i]:r[i]+1]
            sub_nums.sort()
            diff=sub_nums[1]-sub_nums[0]
            count=0
            for j in range(len(sub_nums)):
                if j==len(sub_nums)-1:
                    break
                if(sub_nums[j+1]-sub_nums[j]==diff):
                    count=count+1
            if (count==len(sub_nums)-1):
                answer.append(True)
            else:
                answer.append(False)
        return answer
