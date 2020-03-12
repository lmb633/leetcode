class Solution(object):
    def optimalDivision(self, nums):
        if len(nums)==1:
            return str(nums[0])
        if len(nums)==2:
            return str(nums[0])+'/'+str(nums[1])
        result=str(nums[0])+'/('
        for num in nums[1:-1]:
            result+=str(num)+'/'
        return result+str(nums[-1])+')'