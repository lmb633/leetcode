# 超时
class Solution(object):
    def lastSubstring(self, s):
        max_char = 'a'
        char_idx = []
        for i, char in enumerate(s):
            if char > max_char:
                max_char = char
                char_idx = []
                char_idx.append(i)
            elif char == max_char:
                char_idx.append(i)
        s = s + 'A'
        k = 1
        while len(char_idx) > 1:
            # print(char_idx)
            temp_char = 'a'
            for i in char_idx:
                if s[i + k] > temp_char:
                    temp_char = s[i + k]
            temp_idx = []
            for i in char_idx:
                if s[i + k] == temp_char:
                    temp_idx.append(i)
            char_idx = temp_idx
            # print(char_idx,temp_char)
            k += 1
        return s[char_idx[0]:-1]


# 加了一步合并 勉强通过
class Solution2(object):
    def lastSubstring(self, s):
        max_char = 'a'
        char_idx = []
        for i, char in enumerate(s):
            if char > max_char:
                max_char = char
                char_idx = []
                char_idx.append(i)
            elif char == max_char:
                char_idx.append(i)
        s = s + 'A'
        k = 1
        while len(char_idx) > 1:
            # print(char_idx)
            temp_char = 'a'
            for i in char_idx:
                if s[i + k] > temp_char:
                    temp_char = s[i + k]
            temp_idx = []
            for i in char_idx:
                if s[i + k] == temp_char:
                    temp_idx.append(i)
            char_idx = []
            cur = []
            for idx in temp_idx:
                if not cur:
                    cur = [idx, idx + k]
                elif idx <= cur[1]:
                    cur = [cur[0], idx + k]
                else:
                    char_idx.append(cur[0])
                    cur = [idx, idx + k]
            char_idx.append(cur[0])
            # print(char_idx,temp_char)
            k += 1
        return s[char_idx[0]:-1]


# 双指针法
class Solution3(object):
    def lastSubstring(self, s):
        length = len(s)
        cur_max = length - 1
        left = length - 2
        while left >= 0:
            if s[left] > s[cur_max]:
                cur_max = left
            elif s[left] == s[cur_max]:
                while left - 1 >= 0 and s[left - 1] == s[left]:
                    left -= 1
                flag = 0
                i = 1
                while cur_max + i < length:
                    if s[cur_max + i] > s[left + i]:
                        flag = 1
                        break
                    elif s[cur_max + i] < s[left + i]:
                        break
                    i += 1
                if flag == 0:
                    cur_max = left
            left -= 1

        return s[cur_max:]
