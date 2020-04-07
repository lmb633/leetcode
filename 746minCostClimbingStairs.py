class Solution(object):
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        result = [0] * length
        result[0] = cost[0]
        result[1] = cost[1]
        for i in range(2, length):
            result[i] = min(result[i - 1] + cost[i], result[i - 2] + cost[i])
        return min(result[-1], result[-2])

        """
        :type cost: List[int]
        :rtype: int
        """
