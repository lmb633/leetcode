class Solution(object):
    def lengthOfLIS(self, nums):
        length=len(nums)
        if length==0:
            return 0
        result=[1 for i in range(length)]
        for i in range(length):
            for j in range(i):
                if nums[i]>nums[j]:
                    if result[j]>result[i]-1:
                        result[i]=result[j]+1
        return max(result)

