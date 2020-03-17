class Solution(object):
    def countCharacters(self, words, chars):
        chars_set = {}
        for c in chars:
            if c in chars_set:
                chars_set[c] = chars_set[c] + 1
            else:
                chars_set[c] = 1
        result = 0
        for word in words:
            count = 0
            temp = {}
            for c in word:
                if c in temp:
                    temp[c] = temp[c] + 1
                else:
                    temp[c] = 1
            for c in temp:
                if c in chars_set and temp[c] <= chars_set[c]:
                    count += 1
            if count == len(temp):
                result += len(word)
        return result
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
