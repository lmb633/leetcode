class Solution(object):
    def singleNumber(self, nums):
        diff=0
        for num in nums :
            diff=diff^num
        diff1=diff&(-diff)
        result1=0
        for num in nums:
            if num&diff1:
                result1=result1^num
        return [result1,diff^result1]
        """
        :type nums: List[int]
        :rtype: List[int]
        """