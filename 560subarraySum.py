class Solution(object):
    def subarraySum(self, nums, k):
        pre_dict = {}
        pre_dict[0] = 1
        result = 0
        pre = 0
        for num in nums:
            pre += num
            sub = pre - k
            if sub in pre_dict:
                result += pre_dict[sub]
            if pre in pre_dict:
                pre_dict[pre] += 1
            else:
                pre_dict[pre] = 1
        return result
