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


class Solution2:
    def majorityElement(self, nums):
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == -1:
                candidate = num
                count = 0
        return candidate