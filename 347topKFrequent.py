class Solution(object):
    def topKFrequent(self, nums, k):
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        times_dict = {}
        for num in nums:
            if nums_dict[num] in times_dict:
                times_dict[nums_dict[num]].add(num)
            else:
                times_dict[nums_dict[num]] = set([num])
        # print(times_dict)
        times_list = []
        for times in times_dict:
            times_list += [times] * len(times_dict[times])

        # print(times_list)
        # times_list=[4,4,5,8,1,2,3]
        def quick_sort(nums, low, high, k):
            # print('===',low,high,k)
            temp = nums[low]
            i = low
            j = high
            while i < j:
                while j > i and nums[j] <= temp:
                    j -= 1
                if j >= i:
                    nums[i] = nums[j]
                while i < j and nums[i] > temp:
                    i += 1
                if i <= j:
                    nums[j] = nums[i]
            nums[i] = temp
            # print(i,j)
            if i == k - 1:
                return
            elif i > k - 1:
                quick_sort(nums, low, i - 1, k)
            else:
                quick_sort(nums, i + 1, high, k)

        quick_sort(times_list, 0, len(times_list) - 1, k)
        # print(times_list)

        result = set()
        for i in range(k):
            result = result.union(times_dict[times_list[i]])
        # print(result)
        return list(result)


import heapq


class Solution2(object):
    def topKFrequent(self, nums, k):
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        times_dict = {}
        for num in nums:
            if nums_dict[num] in times_dict:
                times_dict[nums_dict[num]].add(num)
            else:
                times_dict[nums_dict[num]] = set([num])
        times_list = []
        for times in times_dict:
            times_list += [times] * len(times_dict[times])

        topk = heapq.nlargest(k, times_list)
        result = set()
        for top in topk:
            result = result.union(times_dict[top])
        return list(result)