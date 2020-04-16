class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        length = len(height)
        max_height = 0
        max_idx = 0
        for i in range(length):
            if height[i] > max_height:
                max_height = height[i]
                max_idx = i

        def get_half(height):
            max_idx = len(height) - 1
            result = 0
            i = 0
            cur_max = 0
            cur_max_idx = -1
            while i <= max_idx:
                if height[i] < cur_max:
                    i += 1
                else:
                    result += (i - cur_max_idx - 1) * cur_max - sum(height[cur_max_idx + 1:i])
                    cur_max = height[i]
                    cur_max_idx = i
                    i += 1
            return result
        return get_half(height[:max_idx + 1]) + get_half(height[max_idx:][::-1])
