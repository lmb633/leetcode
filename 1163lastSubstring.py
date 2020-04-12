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
