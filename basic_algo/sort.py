# 选择排序
def selcet_sort(nums):
    length = len(nums)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_idx]:
                min_idx = j
        temp = nums[min_idx]
        nums[min_idx] = nums[i]
        nums[i] = temp


# 冒泡排序
def bubble_sort(nums):
    length = len(nums)
    for i in range(length):
        flag = False
        for j in range(1, length - i):
            if nums[j - 1] > nums[j]:
                temp = nums[j - 1]
                nums[j - 1] = nums[j]
                nums[j] = temp
                flag = True
        if not flag:
            break


# 插入排序
def insert_sort(nums):
    length = len(nums)
    for i in range(1, length):
        temp = nums[i]
        j = i
        while j > 0:
            if temp < nums[j - 1]:
                nums[j] = nums[j - 1]
                j -= 1
            else:
                break
        nums[j] = temp


# 快速排序
def quick_sort(nums):
    def sort(nums, left0, right0):
        if left0 >= right0:
            return
        mid = nums[left0]
        left = left0
        right = right0
        while left < right:
            while nums[right] >= mid and left < right:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
            while nums[left] < mid and left < right:
                left += 1
            if left < right:
                nums[right] = nums[left]
                right -= 1
        nums[left] = mid

        sort(nums, left0, left - 1)
        sort(nums, left + 1, right0)

    sort(nums, 0, len(nums) - 1)


# 归并排序
def merge_sort(nums, i, j):
    if i == j:
        return [nums[i]]
    mid = (i + j) / 2
    left = merge_sort(nums, i, mid)
    right = merge_sort(nums, mid + 1, j)
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result


import heapq


# 堆排序
def heap_sort(nums):
    temp = []
    for i in range(len(nums)):
        heapq.heappush(temp, nums[i])
    result = []
    for i in range(len(nums)):
        result.append(heapq.heappop(temp))
    return result


# 基数排序
def radix_sort(nums):
    min_num = min(nums)
    max_num = max(nums)
    if min_num < 0:
        for i in range(len(nums)):
            nums[i] = nums[i] - min_num
        max_num -= min_num
    mod = 1
    while True:
        base = [[] for _ in range(10)]
        for num in nums:
            base[(num // mod) % 10].append(num)
        idx = 0
        # print(base)
        for i in range(10):
            for num in base[i]:
                nums[idx] = num
                idx += 1
        max_num = max_num / 10
        mod *= 10
        if max_num < 1:
            break
    if min_num < 0:
        for i in range(len(nums)):
            nums[i] = nums[i] + min_num
    return nums


# 桶排序
def bucket_sort(nums):
    min_num = min(nums)
    max_num = max(nums)
    gap = (max_num - min_num) // len(nums) + 1
    bucket_num = (max_num - min_num) // gap + 1
    bucket = [[] for _ in range(bucket_num)]
    for num in nums:
        bucket[(num - min_num) // gap].append(num)
    # print(gap,bucket_num, bucket)
    result = []
    for bu in bucket:
        result.extend(sorted(bu))
    return result


# 希尔排序
def shell_sort(nums):
    length = len(nums)
    gap = length // 2
    while gap >= 1:
        for i in range(gap, length):
            temp = nums[i]
            j = i
            while j >= gap:
                if nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                else:
                    break
            nums[j] = temp
        gap = gap // 2
    return nums


# 计数排序
def count_sort(nums):
    min_num = min(nums)
    max_num = max(nums)
    count = [0] * (max_num - min_num + 1)
    for num in nums:
        count[num - min_num] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_num] * c)
    return result


a = [5, 3, 1, 2, 9, 4, 7, 3, 5, 2, 1, 9, 4, 2, 1]
shell_sort(a)
print(a)
