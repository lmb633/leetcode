class Solution(object):
    def insert(self, intervals, newInterval):
        length=len(intervals)
        start=newInterval[0]
        end=newInterval[1]
        i=0
        while i<length and intervals[i][1]<start :
            i+=1
        j=i
        while  j<length and intervals[j][0]<=end :
            j+=1
        if i==length:
            return intervals+[newInterval]
        if j==0:
            return [newInterval]+intervals
        start=min(start,intervals[i][0])
        end=max(end,intervals[j-1][1])
        # print(i,j,end)
        return intervals[:i] + [[start,end]]+intervals[j:]