class MinStack(object):
    def __init__(self):
        self.data = []
        self.minval = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        self.data.append(x)
        self.minval.append(x if not self.minval else min(self.minval[-1], x))

        """
        :type x: int
        :rtype: None
        """

    def pop(self):
        self.data.pop()
        self.minval.pop()
        """
        :rtype: None
        """

    def top(self):
        return self.data[-1]

    """
        :rtype: int
        """

    def getMin(self):
        return self.minval[-1]
        """
        :rtype: int
        """
