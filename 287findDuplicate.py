class Solution(object):
    def findDuplicate(self, nums):
        n=len(nums)-1
        return self.find(nums,1,n)

    def find(self,nums,i,j):
        if i==j:
            return i
        mid=(i+j)//2
        low=0
        for num in nums:
            if i<=num<=mid:
                low+=1
        # print(i,mid,j,low)
        if low>mid-i+1:
            return self.find(nums,i,mid)
        else :
            return self.find(nums,mid+1,j)

        """
        :type nums: List[int]
        :rtype: int
        """