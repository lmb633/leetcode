class Solution(object):
    def merge(self, intervals):
        intervals=sorted(intervals,key=lambda x:x[0])
        result=[]
        for seg in intervals:
            if not result:
                result.append(seg)
            seg0=result[-1]
            if seg0[1]>=seg[0]:
                result.pop()
                result.append([seg0[0],max(seg0[1],seg[1])])
            else:
                result.append(seg)
        return result

        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """