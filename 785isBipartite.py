class Solution(object):
    def isBipartite(self, graph):
        left = set()
        right = set()
        temp = []
        if len(graph) <= 1:
            return True
        i = 0
        while len(graph[i]) == 0:
            i += 1
        if i < len(graph):
            temp.append(i)
        else:
            return False
        while temp:
            temp1 = []
            for node in temp:
                if node in right:
                    return False
                else:
                    left.add(node)
                    for nod in graph[node]:
                        if nod not in left and nod not in right:
                            temp1.append(nod)
            temp = temp1
            left, right = right, left
            if not temp and len(left) + len(right) < len(graph):
                for i in range(len(graph)):
                    if i not in left and i not in right:
                        temp.append(i)
                        break
            print(left, right)
        return True


class Solution1(object):
    def isBipartite(self, graph):
        left = set()
        right = set()
        temp = []
        if len(graph) <= 1:
            return True
        i = 0
        while len(graph[i]) == 0:
            i += 1
        if i < len(graph):
            temp.append(i)
        else:
            return False
        while temp:
            temp1 = []
            for node in temp:
                if node in right:
                    return False
                else:
                    left.add(node)
                    for nod in graph[node]:
                        if nod not in left and nod not in right:
                            temp1.append(nod)
            temp = temp1
            left, right = right, left
            if not temp and len(left) + len(right) < len(graph):
                for i in range(len(graph)):
                    if i not in left and i not in right:
                        temp.append(i)
                        break
            print(left, right)
        return True

graph = [[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14], [], [10], [], [10], [19], [18], [], [16], [15], [23], [23], [], [20, 21], [], [], [27], [26], [],
         [], [34], [33, 34], [], [31], [30, 31], [38, 39], [37, 38, 39], [36], [35, 36], [35, 36], [43], [], [], [40], [], [49], [47, 48, 49], [46, 48, 49], [46, 47, 49],
         [45, 46, 47, 48]]
solution = Solution()
print(solution.isBipartite(graph))
