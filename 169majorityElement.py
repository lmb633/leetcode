class Solution:
    def majorityElement(self, nums):
        mid = len(nums) // 2
        hash_set = {}
        for num in nums:
            if num not in hash_set:
                hash_set[num] = 1
            else:
                hash_set[num] = hash_set[num] + 1
            if hash_set[num] > mid:
                return num
