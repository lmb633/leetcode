class Solution(object):
    def canPartition(self, nums):
        sum_=sum(nums)
        length=len(nums)
        if sum_%2==1:
            return False
        sum_=sum_//2
        result=[[0]*(sum_+1) for i in range(length+1)]
        for i in range(1,length+1):
            for j in range(1,sum_+1):
                if nums[i-1]>j:
                    result[i][j]=result[i-1][j]
                else:
                    result[i][j]=max(result[i-1][j],result[i-1][j-nums[i-1]]+nums[i-1])
        # print(result)
        for i in range(1,length+1):
            if result[i][sum_]==sum_:
                return True
        return False

class Solution2(object):
    def canPartition(self, nums):
        sum_=sum(nums)
        length=len(nums)
        if sum_%2==1:
            return False
        sum_=sum_//2
        result=[[False,]*(sum_+1) for i in range(length+1)]
        result[0][0]=True
        for i in range(1,length+1):
            for j in range(1,sum_+1):
                if nums[i-1]>j:
                    result[i][j]=result[i-1][j]
                else:
                    result[i][j]=result[i-1][j] or result[i-1][j-nums[i-1]]
        # print(result)
        return result[length][sum_]


        """
        :type nums: List[int]
        :rtype: bool
        """



        """
        :type nums: List[int]
        :rtype: bool
        """