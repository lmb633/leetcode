class Solution(object):
    def lastRemaining(self, n, m):
        result=0
        for i in range(1,n+1):
            result=(result+m)%i
        return result