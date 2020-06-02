class Solution(object):
    def checkSubarraySum(self, nums, k):
        pre_dict = {}
        pre_dict[0] = -1
        pre = 0
        for i, num in enumerate(nums):
            pre += num
            if k != 0:
                pre = pre % k
            # print(pre,pre_dict)
            if pre in pre_dict:
                if i - pre_dict[pre] > 1:
                    return True
            else:
                pre_dict[pre] = i
        return False
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
