class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while len(nums)>= nums[i]>0 and nums[i]!=nums[nums[i]-1]:
                # print(i,nums[i],nums[nums[i]-1],nums)
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
                # print(i,nums[i],nums[nums[i]-1],nums)
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1