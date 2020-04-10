import copy


# 超时，没考虑题中单词的长度是相等的，尼玛
class Solution(object):
    def findSubstring(self, s, words):
        length = 0
        word_set = {}
        for word in words:
            length += len(word)
            if word not in word_set:
                word_set[word] = 1
            else:
                word_set[word] += 1

        # word_list.append((word,len(word)))
        # word_list=sorted(word_list,key=lambda x: x[1])

        def is_true(word_set):
            for word in word_set:
                if word_set[word] > 0:
                    return False
            return True

        def check(substr, i0, i, word_set):
            print(i0, i, word_set)
            length = len(substr)
            while i <= length:
                while i <= length and substr[i0:i] not in word_set:
                    i += 1
                temp = substr[i0:i]
                print(i, temp)
                if temp in word_set:
                    word_set[temp] -= 1
                    if i == length and is_true(word_set):
                        print(i, length, True)
                        return True
                    else:
                        flag = check(substr, i, i, word_set)
                        if flag:
                            return True
                        else:
                            word_set[temp] += 1
                            return check(substr, i0, i + 1, word_set)
                else:
                    return False

        i = 0
        result = []
        while i <= len(s) - length:
            print('===============', i, s[i:i + length], '================')
            if check(s[i:i + length], 0, 0, copy.deepcopy(word_set)):
                result.append(i)
            i += 1
        return result


class Solution2(object):
    def findSubstring(self, s, words):
        word_set = {}
        for word in words:
            if word not in word_set:
                word_set[word] = 1
            else:
                word_set[word] += 1

        def is_true(word_set):
            for word in word_set:
                if word_set[word] > 0:
                    return False
            return True

        l = len(words[0])
        length = l * len(words)
        result = []
        i = 0
        while i <= len(s) - length:
            cur_set = copy.deepcopy(word_set)
            for j in range(len(words)):
                tmp = s[i + j * l: i + (j + 1) * l]
                if tmp not in cur_set:
                    break
                else:
                    cur_set[tmp] -= 1
            if is_true(cur_set):
                result.append(i)
            i += 1
        return result


if __name__ == '__main__':
    # s = "aaaaaaaa"
    # words = ["aa", "aa", "aa"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    solution = Solution2()
    print('result', solution.findSubstring(s, words))
