class Solution(object):
    def removeDuplicates(self, nums):
        j=1
        sum_=1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[j]=nums[i+1]
                j+=1
                sum_+=1
        return sum_