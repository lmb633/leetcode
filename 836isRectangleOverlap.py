class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        x1=max(rec1[0],rec2[0])
        y1=max(rec1[1],rec2[1])
        x2=min(rec1[2],rec2[2])
        y2=min(rec1[3],rec2[3])
        return x1<x2 and y1<y2

        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """