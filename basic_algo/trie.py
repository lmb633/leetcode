class Trie(object):
    def __init__(self):
        self.next_ = {}
        self.is_end = False

        """
        Initialize your data structure here.
        """

    def insert(self, word):
        tire = self
        for i, c in enumerate(word):
            if c in tire.next_:
                tire = tire.next_[c]
            else:
                tire.next_[c] = Trie()
                tire = tire.next_[c]
        tire.is_end = True

        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """

    def search(self, word):
        tire = self
        for c in word:
            if c in tire.next_:
                tire = tire.next_[c]
            else:
                return False
        if tire.is_end is True:
            return True
        return False

        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        tire = self
        for c in prefix:
            if c in tire.next_:
                tire = tire.next_[c]
            else:
                return False
        return True
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
