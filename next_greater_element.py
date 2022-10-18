class Solution(object):
    def nextGreaterElement(self,nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            ans=[]
            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    if (nums1[i]==nums2[j] and j<len(nums2)-1):
                        n=1
                        while(j+n<len(nums2)):
                            if (nums2[j+n]>nums2[j]):
                                # print('i',i)
                                # print('j',j)
                                # print('j+n',j+n)
                                ans.append(nums2[j+n])
                            elif(nums2[j+n]<nums2[j] and j+n+1<len(nums2)):
                                n=n+1
                                # print('j+n - e', j+n)
                            else:
                                ans.append(-1)

                            if len(ans)==i+1:
                                  break

                    if nums1[i]==nums2[j] and j==len(nums2)-1:
                        ans.append(-1)
            return ans            
                       
