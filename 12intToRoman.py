class Solution(object):
    def intToRoman(self, num):
        trans_map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        trans_map={v:k for k,v in trans_map.items()}
        print(trans_map)
        numbers=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        result=''
        while num>=1:
            for n in numbers:
                if num>=n:
                    result+=trans_map[n]
                    num-=n
                    break
        return result
        """
        :type num: int
        :rtype: str
        """