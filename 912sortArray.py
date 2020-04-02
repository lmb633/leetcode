# 二路归并排序
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


# 快排
def quick_sort(nums, low, high):
    if low >= high:
        return
    i = low
    j = high
    temp = nums[i]
    while i < j:
        while i < j and nums[j] > temp:
            j -= 1
        if i < j:
            nums[i] = nums[j]
        while i < j and nums[i] <= temp:
            i += 1
        if i < j:
            nums[j] = nums[i]
    nums[i] = temp
    quick_sort(nums, low, i - 1)
    quick_sort(nums, i + 1, high)


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


# shell排序
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


# 后面三种会超时

# 冒泡
def bubble_sort(nums):
    for i in range(len(nums)):
        flag = False
        for j in range(1, len(nums) - i):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                flag = True
        if not flag:
            break
    return nums


# 插入排序
def insert_sort(nums):
    for i in range(1, len(nums)):
        j = i
        temp = nums[i]
        while j > 0:
            if nums[j - 1] > temp:
                nums[j] = nums[j - 1]
                j -= 1
            else:
                break
        nums[j] = temp
    return nums


# 选择排序
def select_sort(nums):
    for i in range(len(nums)):
        idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[idx]:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums


a = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
print(select_sort(a))
