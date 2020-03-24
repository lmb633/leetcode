class Solution(object):
    def massage(self, nums):
        length=len(nums)
        if length==0:
            return 0
        if length<=2:
            return max(nums)
        result=[nums[0],max(nums[:2])]
        for i in range(2,length):
            temp=max(result[i-2]+nums[i],result[i-1])
            result.append(temp)
        return result[-1]
