class Solution(object):
    def findRestaurant(self, list1, list2):
        map1 = {}
        i = 0
        for r in list1:
            map1[r] = i
            i += 1
        i = 0
        min_index = 1000000
        map2 = {}
        for r in list2:
            if r in map1:
                if i + map1[r] < min_index:
                    min_index = i + map1[r]
                map2[r] = i + map1[r]
            i += 1
        result = []
        for r in map2:
            if map2[r] == min_index:
                result.append(r)
        return result
