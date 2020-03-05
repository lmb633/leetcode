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


def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp


a = [5, 3, 1, 2, 9, 4, 7, 3, 5, 2, 1, 9, 4, 2, 1]
quick_sort(a)
print(a)
