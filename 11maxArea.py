# 笨方法  当数列递增时超时
class Solution(object):
    def maxArea(self, height):
        left = {}
        left[0] = height[0]
        max_left = left[0]
        max_area = 0
        for i, r_h in enumerate(height[1:]):
            for j, l_h in left.items():
                h = min(r_h, l_h)
                area = h * (i + 1 - j)
                if area > max_area:
                    max_area = area
            if r_h > max_left:
                left[i + 1] = r_h
                max_left = r_h
        return max_area


class Solution2(object):
    def maxArea(self, height):
        length = len(height)
        max_area = 0
        i = 0
        j = length - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


solution = Solution2()
length = [1, 2,3,4]
print(solution.maxArea(length))
