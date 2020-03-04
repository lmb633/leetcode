class Solution(object):
    def minSubArrayLen(self, s, nums):
        temp_sum=0
        min_length=2**32-1
        i=0
        j=0
        while j<len(nums) and i<=j:
            while temp_sum<s and j<len(nums):
                temp_sum+=nums[j]
                j+=1
            while temp_sum>=s:
                if min_length>j-i:
                    # print(min_length,i,j)
                    min_length=j-i
                temp_sum-=nums[i]
                i+=1
        return 0 if min_length==2**32-1 else min_length