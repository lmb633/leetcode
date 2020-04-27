class Solution(object):
    def palindromePairs(self, words):
        words = {words[i]: i for i in range(len(words))}
        print(words)

        def valid_prefix(word):
            length = len(word)
            prefix = []
            for i in range(length):
                mid = (length + i) // 2
                if (length - i) % 2 == 1:
                    if word[i:mid] == word[-1:mid:-1]:
                        prefix.append(word[:i])
                else:
                    if word[i:mid] == word[-1:mid - 1:-1]:
                        prefix.append(word[:i])
            prefix.append(word)
            return prefix

        def get_pairs(words, result, flag=0):
            for word in words:
                prefix = valid_prefix(word)
                print(word, prefix)
                for valid in prefix:
                    valid = valid[::-1]
                    if valid in words and valid != word:
                        if flag == 0:
                            result.add((words[word], words[valid]))
                        else:
                            result.add((words[valid], words[word]))

        result = set()
        get_pairs(words, result)
        words = {k[::-1]: v for k, v in words.items()}
        get_pairs(words, result, 1)
        return result


a = ["abcd", "dcba", "lls", "s", "sssll"]
solution = Solution()
print(solution.palindromePairs(a))
