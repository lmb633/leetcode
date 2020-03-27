import math


class Solution(object):
    def hasGroupsSizeX(self, deck):
        if len(deck) < 2:
            return False
        deck_set = {}
        for d in deck:
            if d in deck_set:
                deck_set[d] = deck_set[d] + 1
            else:
                deck_set[d] = 1
        gcd_ = None
        for k in deck_set:
            if gcd_ is None:
                gcd_ = deck_set[k]
            gcd_ = math.gcd(gcd_, deck_set[k])
        if gcd_ < 2:
            return False
        return True

        """
        :type deck: List[int]
        :rtype: bool
        """
